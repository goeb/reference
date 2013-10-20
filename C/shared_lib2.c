
/* 
 * gcc -fPIC -c shared_lib2.c
 * gcc -shared -Wl,-soname,libf2.so -o libf2.so shared_lib2.o
 *
 */
#include <stdio.h>

#include "shared_lib.h"
//#include "shared_object.h"

void myFuncOfLuxuous(void)
{
	printf("myFuncOfLuxuous()\n");
}

void run(int x)
{
	printf("Starting... [x=%d]\n", x);
	display_doc_0();
	printf("Stopping...\n");
//	shared_func();
}
