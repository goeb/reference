
/* 
 * gcc 3_threads.c -lpthread
 **/

#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>



void * f(void *p) {
	long id;
	int i;
	id = (long int)syscall(224);
	printf("thread[%ld]: starting...\n", id);
	for (i=0; i<10; i++) {
		printf("thread[%ld]:i=%d\n", id, i);
		sleep(1);
	}	
	sleep(1);
	printf("thread[%ld]: ending...\n", id);
	exit(3);
}

void * g(void *p) {
	printf("g: starting...\n");
	sleep(3);
	printf("g: exiting...\n");
	exit(0);
}

main() {
	pthread_t t1, t2, t3, t4;
	pthread_create(&t1, NULL, &f, 0);
	pthread_create(&t2, NULL, &f, 0);
	pthread_create(&t3, NULL, &f, 0);
	pthread_create(&t4, NULL, &g, 0);
	printf("main: threads launched\n");
	sleep(20);
	printf("main: terminated\n");
}
