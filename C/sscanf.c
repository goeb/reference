
#include <stdio.h>
#include <stdlib.h>

main(int argc, char ** argv)
{
	int x;
	char output[5+1];
	int n = sscanf(argv[1], "0x%5s", output);
	printf("sscanf(%s): n=%d, output=%s\n", argv[1], n, output);
}
