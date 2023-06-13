#include <errno.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
	if (argc != 2) {
		fprintf(stderr, "usage: %s <file>\n", argv[0]);
		return 1;
	}

	char resolved_path[PATH_MAX];
	printf("Using buffer of size PATH_MAX=%d\n", PATH_MAX);
	char *ptr = realpath(argv[1], resolved_path);
	if (!ptr) {
		fprintf(stderr, "realpath error: %s\n", strerror(errno));
		return 1;
	}

	printf("%s\n", ptr);
}
