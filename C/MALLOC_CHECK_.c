/*
 * export MALLOC_CHECK_=1
 */

#include <stdio.h>
#include <stdlib.h>

main() {

	char * x = (char *) malloc(4);
	//memcpy((void*)x, "tototooto", 15);
	//*(x-1) = 'x';
	free(x);


	printf("end.\n");
	abort();

}
