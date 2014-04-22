#include <stdio.h>
#include <sys/eventfd.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <errno.h>

int main()
{
	//printf("EFD_NONBLOCK=%d\n", EFD_NONBLOCK);
	int controlIndicationFd = eventfd(0, 0x800); //EFD_NONBLOCK); because EFD_NONBLOCK not compiling on ARM
	if (controlIndicationFd < 0) {
		printf("Could not create event FD: %s\n", strerror(errno));
		return 1;
	}

	printf("xxx\n");
	eventfd_t x = 2;
	int y;
	eventfd_write(controlIndicationFd, x);
	eventfd_write(controlIndicationFd, x);
	printf("written\n");
	y = eventfd_read(controlIndicationFd, &x);
	printf("1. x=%llu, y=%d\n", x, y);
	eventfd_write(controlIndicationFd, 1);
	y = eventfd_read(controlIndicationFd, &x);
	printf("2. x=%llu, y=%d\n", x, y);
	y = eventfd_read(controlIndicationFd, &x);
	printf("3. x=%llu, y=%d\n", x, y);
}

