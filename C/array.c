
#include <errno.h>
#include <string.h>
char *strerror(int errnum);

/* you can think of it as being implemented like this: */
static char strerror_buf[1024];
const char *sys_errlist[] = {
    [EPERM]  = "Operation not permitted",
    [ENOENT] = "No such file or directory",
    [ESRCH]  = "No such process",
    [EINTR]  = "Interrupted system call",
    [EIO]    = "I/O error",
    [ENXIO]  = "No such device or address",
    [E2BIG]  = "Argument list too long",
    /* etc. */
};
const int array[] = {
    [1] = 111,
    [5] = 555,
};

main()
{
	printf("array[5] = %d\n", array[5]);
}
