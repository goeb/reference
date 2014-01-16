       #include <sys/types.h>
       #include <sys/stat.h>
       #include <fcntl.h>

#include <unistd.h>

main()
{
	int f = open("xxx", O_APPEND|O_WRONLY|O_SYNC);
	write(f, "toto\n", 5);
	//fsync(f);
	//fdatasync(f);
	close(f);
	//fsync(f);
}

