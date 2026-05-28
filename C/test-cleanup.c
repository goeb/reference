//
// This shows how to use __attribute __cleanup__ to get a callback executed
// when a variable goes out of scope.
// 
// Compilation:
// gcc -o test-cleanup test-cleanup.c
//
// Execution:
// ./test-cleanup 
// main starts
// test_cleanup: x=33
// cleanup_function: x=33
// main ends

#include <stdio.h>
#include <stdlib.h>

void cleanup_function(int *x)
{
		printf("cleanup_function: x=%d\n", *x);
}


int test_cleanup()
{
	int x   __attribute ((__cleanup__(cleanup_function)));
	x = 33;
	printf("test_cleanup: x=%d\n", x);
	return 0;
}

int main()
{
	printf("main starts\n");
	test_cleanup();
	printf("main ends\n");
}
