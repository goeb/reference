       #include <sys/types.h>
       #include <sys/stat.h>
       #include <fcntl.h>

main()
{
	//int fd = creat("xxx", S_IRUSR|S_IWUSR|S_IRGRP|S_IROTH);
	int fd = creat("xxx", 0644);


}
