#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <errno.h>

int main(int argc, char ** argv) {

	if (argc != 4) {
		fprintf(stderr, "Usage: %s file count bs\n", argv[0]);
		exit(1);
	}
	const char* file = argv[1];
	int count = atoi(argv[2]);
	int bs = atoi(argv[3]);
	fprintf(stderr, "starting: file=%s count=%d bs=%d\n", file, count, bs);

	int f = open(file, O_WRONLY|O_CREAT|O_TRUNC);
	if (f < 0) {
		fprintf(stderr, "Cannot open file %s: %s\n", file, strerror(errno));
		exit(1);
	}

	char * ones = (char*) malloc(bs);
	memset(ones, 0xFF, bs);

	while (count>0) {
		int n = write(f, ones, bs);
		if (n != bs) {
			fprintf(stderr, "Cannot write more than n=%d : %s\n", n, strerror(errno));
			exit(1);
		}
		count--;
	}

	free(ones);
}
