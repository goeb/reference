#include <stdio.h>

#include <sys/types.h>
#include <fcntl.h>

int main (int argc, char **argv)
{
	int fd;
	int length;
	
	if (argc != 2) return 1;
	fd = open(argv[1], O_RDONLY);
	length = lseek(fd, 0, SEEK_END);
	printf("length of %s: %d\n", argv[1], length);
	return 0;
}
