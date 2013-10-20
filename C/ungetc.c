#include <stdio.h>

int readchar(FILE *fd, int indicator)
{
	int c;
	c = fgetc(fd);
	printf("read : %c (indic=%d)\n", c, indicator);
	if (indicator==1) ungetc(c, fd);
}

main()
{
	FILE *fd;

	fd = fopen("toto", "r");
	readchar(fd, 0);
	readchar(fd, 0);
	readchar(fd, 0);
	readchar(fd, 1);
	readchar(fd, 0);
	readchar(fd, 0);
	readchar(fd, 0);
	readchar(fd, 1);
	readchar(fd, 0);
}
