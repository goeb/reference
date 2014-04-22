#include <stdlib.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>

void usage()
{
	printf("Usage: \n"
			"    a.out mode [file]\n"
			"\n"
			"mode :== F_RDLCK | F_WRLCK\n");
	exit(1);
}


int main (int argc, char* argv[])
{
	char* file;

	if (argc < 2) usage();
	if (argc > 2) file = argv[2]; // lock file given as argument
	else file = argv[0]; // lock myself

	// get mode
	short type;
	if (0 == strcmp(argv[1], "F_RDLCK")) type = F_RDLCK;
	else if (0 == strcmp(argv[1], "F_WRLCK")) type = F_WRLCK;
	else usage();

	int fd;
	int flags;
	struct flock lock;
    struct flock fd_lock = {
        .l_start = 0,
        .l_len = 0,
        .l_whence = SEEK_SET,
        .l_type = type
    };


	printf("Opening file %s... ", file);
    fd = open(file, O_RDONLY);
    if (fd < 0) {
        printf("failed to open config file %s: %s\n", file, strerror(errno));
        return 1;
    }
	printf("ok\n");

    if ((flags = fcntl(fd, F_GETFD)) == -1) {
        printf("Could not retrieve flags from file %s\n", file);
        close(fd);
        return 1;
    }
    flags |= FD_CLOEXEC;
    if (fcntl(fd, F_SETFD, flags) == -1) {
        printf("Could not set flags on file %s\n", file);
        close(fd);
        return 1;
    }
    /* We don't want anybody to change the file while we parse it,
     * let's try to lock it for reading. */
	printf("Locking file... ");
    if (fcntl(fd, F_SETLK, &fd_lock) == -1) {
		printf("Could not lock file %s %s\n", file, argv[1]);
    } else printf("ok\n");

	printf("hit enter...");
	getchar();

	close(fd);
	return 0;
}

