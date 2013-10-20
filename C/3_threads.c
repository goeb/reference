
/* 
 * gcc 3_threads.c -lpthread
 **/

#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>


void * f(void *p) {
	printf("f: starting...\n");
	sleep(2);
	printf("f: ending...\n");
	exit(3);
}

void * g(void *p) {
	printf("g: starting...\n");
	sleep(10);
	printf("g: ending...\n");
}

void * h(void *p) {
	printf("h: starting...\n");
	sleep(10);
	printf("h: ending...\n");
}


main() {
	pthread_t t1, t2, t3;
	pthread_attr_t attr;
	int rc;
	pthread_create(&t1, NULL, &f, 0);
	pthread_create(&t2, NULL, &g, 0);
	pthread_create(&t3, NULL, &h, 0);
	printf("main: threads launched\n");
	sleep(10);
	printf("main: terminated\n");
}
