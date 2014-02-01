       #include <sys/types.h>
       #include <sys/stat.h>
       #include <fcntl.h>
#include <stdio.h>

main()
{
	int fd = open("yutui", O_WRONLY |O_TRUNC);
	printf("fd=%d\n", fd);
}
