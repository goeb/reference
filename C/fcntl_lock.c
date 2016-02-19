#include <errno.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int lockFile(const char *path)
{
    int flags = O_WRONLY|O_CREAT|O_CLOEXEC;
    int mode = 0666;
    int fd = open(path, flags, mode);

    if (fd < 0) {
        printf("Cannot create file '%s' for locking: %s\n", path, strerror(errno));
        return -1;
    }

    struct flock lockParams;
    lockParams.l_type = F_WRLCK;
    lockParams.l_len = 0;
    lockParams.l_pid = 0;
    lockParams.l_start = 0;
    lockParams.l_whence = SEEK_SET;

    int r = fcntl(fd, F_SETLK, &lockParams);
    if (r != 0) {
        printf("Cannot lock file '%s' (%d): %s (owned by puid %d)\n", path, fd, strerror(errno), lockParams.l_pid);
        close(fd);
        return -1;
    }
    return fd;
}
void unlockFile(int fd)
{
    struct flock lockParams;
    lockParams.l_type = F_UNLCK;
    lockParams.l_len = 0;
    lockParams.l_pid = 0;
    lockParams.l_start = 0;
    lockParams.l_whence = SEEK_SET;

    int r = fcntl(fd, F_SETLK, &lockParams);
    if (r != 0) {
        printf("Cannot unlock file '%d': %s\n", fd, strerror(errno));
    }
    close(fd);
}

int main()
{
    int fd = lockFile("toto");
    if (fd < 0) return 1;
    sleep(10);
    printf("unlock\n");
    unlockFile(fd);
    sleep(10);
}

