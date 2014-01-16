#include <stdio.h>
#include <sys/file.h>

int main(int argc, char ** argv) 
{
	int fd = open(argv[1], O_CREAT|O_RDONLY);
	int r = flock(fd, LOCK_EX|LOCK_NB);
	printf("flock returned: %d\n", r);
	printf("sleeping 10...\n");
	sleep(10);
	printf("done.\n");
}
