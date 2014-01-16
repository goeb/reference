#include <stdio.h>
main() 
{
	int x = -0xFF;
	unsigned y = x;
	printf("x=%x, y=%x\n", x, y);

	int x2 = x << 1;
	int x3 = x >> 1;
	printf("x2=%x, x3=%x\n", x2, x3);
}
