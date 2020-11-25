#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <pty.h>
#include <termios.h>
#include <sys/select.h>

int main()
{

	int master;
	pid_t pid;

	pid = forkpty(&master, NULL, NULL, NULL);

	// impossible to fork
	if (pid < 0) {
		return 1;

	} else if (pid == 0) {
		// child

		char *args[] = { NULL };

		// run something
		// t.sh could be something like:
		// #!/bin/sh
		// socat - PTY,link=/tmp/xtty,cfmakeraw
		execvp("/tmp/t.sh", args);

	} else {
		// parent

		// remove the echo
		struct termios tios;
		tcgetattr(master, &tios);
		tios.c_lflag &= ~(ECHO | ECHONL);
		tcsetattr(master, TCSAFLUSH, &tios);

		for (;;) {

			fd_set read_fd;
			fd_set write_fd;

			FD_ZERO(&read_fd);

			FD_SET(master, &read_fd);
			FD_SET(STDIN_FILENO, &read_fd);

			select(master+1, &read_fd, NULL, NULL, NULL);

			char input;
			char output;

			if (FD_ISSET(master, &read_fd)) {
				// read from the child process
				ssize_t n = read(master, &output, 1);
				if (-1 == n) break;

				write(STDOUT_FILENO, &output, 1);
			}

			if (FD_ISSET(STDIN_FILENO, &read_fd)) {
				// read from stdin
				read(STDIN_FILENO, &input, 1);
				if (input == 'q') {
					printf("exiting... (q)\n");
					break;
				}
				write(master, &input, 1);
			}
		}
	}
	return 0;
}
