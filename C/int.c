#include <limits.h>
#include <stdio.h>

int x = INT_MAX;
int ux = UINT_MAX;

main()
{
	unsigned long long int y = x + ux;
	printf("x=%d, ux=%u, y=%llu\n", x, ux, y);
}
