
#include <stdio.h>

main() {

	unsigned int a = 3000000000;
	unsigned int b = 4000000000;
	unsigned long long c = a + b;

	printf("a=%u, b=%u, c=%llu\n", a, b, c);
	printf("a=%x, b=%x, c=%llx\n", a, b, c);
}
