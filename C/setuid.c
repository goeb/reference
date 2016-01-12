#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main()
{
	int r = setuid(0);
	printf("setuid(0)=%d, %s\n", r, strerror(errno));

	r = system("id");
}


