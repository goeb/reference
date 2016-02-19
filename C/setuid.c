#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main()
{
	system("id");
	system("touch toto_before_setuid");

	int r = setuid(0);
	printf("setuid(0)=%d, %s\n", r, strerror(errno));

	system("id");
	system("touch toto_after_setuid");
}


