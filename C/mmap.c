
#include <sys/types.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(void)
{
	int fd = -1;
	char *filename = "t.txt";

	printf("opening file: %s\n", filename);
	if ((fd = open(filename, O_RDWR, 0)) == -1) {
		perror("open");
		return 1;
	}

	char *data = mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0);

	if (data == MAP_FAILED) {
		perror("mmap");
		return 1;
	}

	printf("First 6 bytes: ");
	fflush(stdout);
	write(1, data, 6);
	printf("\n");
	printf("Replacing first 6 bytes...\n");
	strcpy(data, "hello\n");

	munmap(data, 4096);
	close(fd);
	return EXIT_SUCCESS;
}
