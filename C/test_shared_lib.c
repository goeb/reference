
/*
 * gcc test_shared_lib.c -o test_shared_lib -L. -lfff
 * export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
 */
#include <stdio.h>
#include "shared_lib.h"

main() {
	printf("tototo\n");
	display_doc();
}
