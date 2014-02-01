
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

main()
{
	int fd = open("/dev/tty", O_RDWR|O_NOCTTY|O_NONBLOCK);
	write(fd, "toto\n");
}
