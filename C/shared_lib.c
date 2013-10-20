
/* 
 * gcc -fPIC -c shared_lib.c
 * gcc -shared -Wl,-soname,libfff.so -o libfff.so shared_lib.o
 *
 */
#include <stdio.h>
//#include "shared_object.h"

void shared_func(void)
{
	printf("shared_lib.c: shared_func()");
}
void display_doc_0(void) {
	printf("display_doc_0: yoyo\n");
	shared_func();
}
void display_doc(void) {
	printf("display_doc: yoyo\n");
	printf("display_doc: version 2\n");
}
