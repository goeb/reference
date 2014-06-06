
#include <stdio.h>
#include <stdlib.h>

main(int argc, char ** argv)
{
	printf("x=%d\n", atoi(argv[1]));
	printf("atoi(\"\")=%d\n", atoi(""));
}
