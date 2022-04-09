
#include <argp.h>
#include <errno.h>
#include <fcntl.h>
#include <poll.h>
#include <pty.h>
#include <signal.h>
#include <spawn.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <termios.h>
#include <unistd.h>

const char *VERSION = "ptyexec-1.0";

void usage()
{
	printf("Usage: ptyexec [--merge-stderr] COMMAND ...\n"
	       "\n"
	       "Ptyexec runs a program (called \"server\") and connects its stdin, stdout\n"
	       "(and optionally its stderr) to a PTY. Another program (called \"client\") can\n"
	       "interact with the server by writing to and reading from the PTY file.\n"
	       "\n"
	       "At startup ptyexec prints on its STDOUT the file name of the PTY.\n"
	       "\n"
	       "Options:\n"
	       "    --merge-stderr   Redirect the STDERR of the server to the PTY as well\n"
	       "                     (by default STDERR of the server is printed to the STDERR of\n"
           "                     ptyexec itself).\n"
	       "\n"
	       "Example:\n"
	       "    $ ptyexec sh -c 'while true; do read line; echo line=[$line]; done'\n"
	       "    /dev/pts/16\n"
	       "\n"
	       "    $ echo hello world > /dev/pts/16\n"
	       "    $ cat /dev/pts/16\n"
	       "    line=[hello world]\n"
	       "\n");
	exit(1);
}

void info(char *format, ...)
{
    va_list args;
    va_start(args, format);
    vfprintf(stderr, format, args);
    va_end(args);

	fprintf(stderr, "\n");
}


static pid_t Child_Pid = -1;

void terminate_child(pid_t child_pid)
{
	if (child_pid <= 0) {
		info("terminate_child: invalid pid %d", child_pid);
		return;
	}

	int err = kill(child_pid, SIGTERM);
	if (-1 == err) {
		info("kill error: %s", strerror(errno));
		return;
	}
	
	// Wait and collect the exit status of the child
	int status;
	err = waitpid(child_pid, &status, 0);	
	if (-1 == err) info("waitpid error: %s", strerror(errno));

	if (WIFEXITED(status)) {
		info("child terminated with exit status %d", WEXITSTATUS(status));
	} else if (WIFSIGNALED(status)) {
		info("child killed by signal %d", WTERMSIG(status));
	} else {
		info("waitpid returned unknown status: %d", status);
	}
}


void die(char *format, ...)
{
	va_list args;
	va_start(args, format);
	vfprintf(stderr, format, args);
	va_end(args);

	fprintf(stderr, "\n");

	if (Child_Pid > 0) terminate_child(Child_Pid);
	exit(1);
}


void set_flag_cloexec(int fd)
{
	int flags = fcntl(fd, F_GETFD);
	if (-1 == flags) die("fcntl GETFD error: %s", strerror(errno));

	flags |= FD_CLOEXEC;

	int err = fcntl(fd, F_SETFD, flags);
	if (err) die("fcntl SETFD error: %s", strerror(errno));
}

int setup_pty()
{
	int fd_master = 0;
	int fd_slave = 0;
	int err = openpty(&fd_master, &fd_slave, 0, 0, 0);

	if (err) die("openpty error: %s", strerror(errno));

	// Print the file name of the PTY
	char name[1024];
	err = ttyname_r(fd_slave, name, sizeof(name));
	if (err) die("ttyname_r error: %s", strerror(errno));

	// Print the file name to stdout
	printf("%s\n", name);

	// Disable echo and adding of character '\r' at end of line
	struct termios tios;
	cfmakeraw(&tios);
    err = tcsetattr(fd_slave, TCSANOW, &tios);
    if (err) die("tcsetattr error: %s", strerror(errno));

	// Set flag FD_CLOEXEC so that the child does not inherit the file descriptors
	set_flag_cloexec(fd_master);
	set_flag_cloexec(fd_slave);

	return fd_master;
}


pid_t start_child_process(int argc, char **argv, int *child_stdin, int *child_stdout, int *child_stderr)
{
	int err = 0;

    int pipe_child_stdin[2];
    int pipe_child_stdout[2];
    int pipe_child_stderr[2];
	err |= pipe(pipe_child_stdin);
	err |= pipe(pipe_child_stdout);
	err |= pipe(pipe_child_stderr);
    if (err) die("pipe error: %s", strerror(errno));

    posix_spawn_file_actions_t actions;
    err = posix_spawn_file_actions_init(&actions);
	if (err) die("posix_spawnattr_init error: %s", strerror(err));

	// redirect stdin
    err |= posix_spawn_file_actions_addclose(&actions, pipe_child_stdin[1]);
    err |= posix_spawn_file_actions_adddup2(&actions, pipe_child_stdin[0], 0);
    err |= posix_spawn_file_actions_addclose(&actions, pipe_child_stdin[0]);
	*child_stdin = pipe_child_stdin[1]; // for the parent process

	// redirect stdout
    err |= posix_spawn_file_actions_addclose(&actions, pipe_child_stdout[0]);
    err |= posix_spawn_file_actions_adddup2(&actions, pipe_child_stdout[1], 1);
    err |= posix_spawn_file_actions_addclose(&actions, pipe_child_stdout[1]);
	*child_stdout = pipe_child_stdout[0]; // for the parent process

	// redirect stderr
    err |= posix_spawn_file_actions_addclose(&actions, pipe_child_stderr[0]);
    err |= posix_spawn_file_actions_adddup2(&actions, pipe_child_stderr[1], 2);
    err |= posix_spawn_file_actions_addclose(&actions, pipe_child_stderr[1]);
	*child_stderr = pipe_child_stderr[0]; // for the parent process

	if (err) die("posix_spawn_file_actions error: %s", strerror(err));

	posix_spawnattr_t attr;
	err = posix_spawnattr_init(&attr);
	if (err) die("posix_spawnattr_init error: %s", strerror(err));

    // In the child process:
    // - Unblock all signals
    //   (POSIX_SPAWN_SETSIGMASK + sigemptyset + posix_spawnattr_setsigmask)
    // - Reset to the default the dispositions of any signals that are being
    //   caught (ignored signals, etc.)
    err = posix_spawnattr_setflags(&attr, POSIX_SPAWN_SETSIGMASK);
    if (err) die("posix_spawnattr_setflags error: %s", strerror(err));

    sigset_t mask;
    sigemptyset(&mask);
    err = posix_spawnattr_setsigmask(&attr, &mask);
    if (err) die("posix_spawnattr_setsigmask error: %s", strerror(err));

	char **envp = 0;
	pid_t child_pid;

    err = posix_spawnp(&child_pid, argv[0], &actions, &attr, argv, envp);
    if (err) die("posix_spawnp error: %s", strerror(err));

	close(pipe_child_stdin[0]);
	close(pipe_child_stdout[1]);
	close(pipe_child_stderr[1]);

	return child_pid;
}

enum Direction { PTY_TO_CHILD, CHILD_TO_PTY, CHILD_TO_STDERR };

void copy_bytes(enum Direction direction, int src, int dest)
{
		char buffer[1024];
		const char* label = 0;
		if (direction == PTY_TO_CHILD) label = "pty->child";
		else if (direction == CHILD_TO_PTY) label = "child->pty";
		else label = "child->stderr";

		int n = read(src, buffer, sizeof(buffer));

		if (n == 0) {
			// peer end closed ?
			if (direction == PTY_TO_CHILD) die("read error (%s): %s", label, strerror(errno)); // should not happen
			// else CHILD_TO_PTY or CHILD_TO_STDERR
			die("read error (%s): %s", label, strerror(errno)); // child terminated ?
		}
		if (n < 0) die("read error (%s): %s", label, strerror(errno));
		// else : n > 0)

		// Copy to child_stdin
		int err = write(dest, buffer, n);
		if (-1 == err) die("write error (%s): %s", label, strerror(errno));
}


int main(int argc, char **argv)
{
	int merge_stderr = 0;

	// Parse command line arguments
	if (argc < 1) die("argc < 1");
	argc--; argv++;

	if (argc >= 1 && 0 == strcmp(argv[0], "--merge-stderr")) {
		merge_stderr = 1;
		argc--; argv++;
	}

	if (argc < 1) usage();

	// The remaining arguments are the command and its arguments
	
	int fd_master_pty = setup_pty();

	int child_stdin;
	int child_stdout;
	int child_stderr;
	Child_Pid = start_child_process(argc, argv, &child_stdin, &child_stdout, &child_stderr);

	info("child: %d", Child_Pid);

	// Transfer bytes from fd_master_pty to the stdin of the child process
	// Trasnfer bytes from the stdout (otpionally stderr) of the child process to fd_master_pty

	struct pollfd poll_fds[3] = {
		{ .fd=fd_master_pty, .events=POLLIN },
		{ .fd=child_stdout,  .events=POLLIN },
		{ .fd=child_stderr,  .events=POLLIN }
	};
	
	while (1) {
		int err = poll(poll_fds, 3, 1000);

		if (err == -1) die("poll error: %s", strerror(errno));

		if (err == 0) {
			// timeout, no byte received
			continue;
		}

		if (poll_fds[0].revents & POLLIN) {
			// At least 1 byte or event received on fd_master_pty
			copy_bytes(PTY_TO_CHILD, fd_master_pty, child_stdin);

		} else if (poll_fds[1].revents & POLLIN) {
			// At least 1 byte or event received from the child stdout
			copy_bytes(CHILD_TO_PTY, child_stdout, fd_master_pty);

		} else if (poll_fds[2].revents & POLLIN) {
			// At least 1 byte or event received from the child stderr
			if (merge_stderr) {
				copy_bytes(CHILD_TO_PTY, child_stderr, fd_master_pty);
			} else {
				copy_bytes(CHILD_TO_STDERR, child_stderr, 2);
			}
		} else if ( (poll_fds[1].revents & POLLHUP) || (poll_fds[2].revents & POLLHUP) ) {
			// Pipe closed by child
			break;
		}
	}

	terminate_child(Child_Pid);

	return 0;
}
