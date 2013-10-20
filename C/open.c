#include <fcntl.h>
#include <errno.h>
#include <string.h>

main() {
    int fd;
    fd = open("xxx.x", O_CREAT|O_WRONLY|O_EXCL, 777);
    printf("errno=%d, %s\n", errno, strerror(errno));
    close(fd);
}

