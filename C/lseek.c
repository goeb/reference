#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


main ()
{
	int fd;
	int length;

	fd = open ("toto", O_RDONLY);
	length = lseek (fd, 0, SEEK_END);
	printf ("length : %d\n", length);
}
