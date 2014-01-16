
#include <stdio.h>
#include <errno.h>
#include <string.h>

main() {
	printf("%s\n", strerror(EAGAIN));
}
