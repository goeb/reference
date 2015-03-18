
/* 
 * gcc threads.c -lpthread
 **/

#include <stdio.h>
#include <pthread.h>

typedef struct {
	int value;
	pthread_mutex_t mutex;
} shared_stack_t;

void * f(void *p) {
	int rc;
	shared_stack_t *shared_stack = (shared_stack_t *)p;
	printf("f: starting...(%d==%x)\n", pthread_self(), pthread_self());
	while (1) {
		printf("f: waiting for lock\n");
		rc = pthread_mutex_lock(&shared_stack->mutex);
		printf("f: unblocked\n");
		printf("f: value=%d\n", shared_stack->value);
		rc = pthread_mutex_unlock(&shared_stack->mutex);
	}

}


main() {
	shared_stack_t shared_stack;
	pthread_t thread;
	pthread_attr_t attr;
	int rc;
	/* init shared_stack */
	shared_stack.value = 33;
	rc = pthread_mutex_init(&shared_stack.mutex, NULL);

	rc = pthread_mutex_lock(&shared_stack.mutex);
	pthread_create(&thread, NULL, &f, &shared_stack);
	sleep(2);
	rc = pthread_mutex_unlock(&shared_stack.mutex);
	while (1) {
		rc = pthread_mutex_lock(&shared_stack.mutex);
		printf("main: lock rc=%d\n", rc);
		sleep(1);
		shared_stack.value ++;
		printf("main: push value %d (unlock)\n", shared_stack.value);
		rc = pthread_mutex_unlock(&shared_stack.mutex);
		printf("main: unlock rc=%d\n", rc);
		for (rc=0; rc<10; rc++) printf(".");
		printf("\n");
	}
}
