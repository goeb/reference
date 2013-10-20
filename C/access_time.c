#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

void usage_and_exit(char *s)
{
	fprintf(stderr, "Usage : %s file\n", s);
	exit(-1);
}
main (int argc, char **argv)
{
	struct stat buf;
	int rc;
	if (argc != 2) usage_and_exit(argv[0]);
	if (0 != stat(argv[1], &buf)) {
		perror(argv[1]);
		exit(-1);
	}
	printf("%d\n", buf.st_atime);
	exit(0);
}

