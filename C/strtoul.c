#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

void test(const char *str)
{
	unsigned long int n = strtoul(str, 0, 10);
	printf("%30s: n=%lu, ULONG_MAX=%lu, errno=%d\n", str, n, ULONG_MAX, errno);
}

int main()
{
	test("a123456789");
	test("123456789");
	test("333b");
	test("12\n3456789");
	test("12345678901");
	test("4294967295");
	test("4294967296");
	test("-55");
	test("-4294967296");
}
