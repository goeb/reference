
#include <stdio.h>
#include <stdint.h>

main() {

	unsigned int a = 3000000000;
	unsigned int b = 4000000000;
	unsigned long long c = a + b;

	printf("a=%u, b=%u, c=%llu\n", a, b, c);
	printf("a=%x, b=%x, c=%llx\n", a, b, c);

	int second = 62114;
	int day = 35330;
	int64_t date;
	date = second + day * 86400;
	printf("date=%lld\n", date);
	date = (int64_t)second + day * 86400;
	printf("date=%lld\n", date);
	date = (int64_t)(second + day * 86400);
	printf("date=%lld\n", date);
	date = (int64_t)second + (int64_t)day * 86400;
	printf("date=%lld\n", date);
}
