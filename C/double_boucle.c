
#include <stdio.h>

main()
{
	// test of index reused in inner loop
	// => infinite loop !!!
	int i;
	for (i=0; i<10; i++) {
		for (i=0; i<5; i++) {
			printf(".");
		}
	}
}
