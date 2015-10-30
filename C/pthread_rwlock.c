
/* 
 * gcc threads.c -lpthread
 **/

#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

typedef struct {
	int value;
	pthread_rwlock_t mutex;
} shared_stack_t;

void * f(void *p) {
	int rc;
	shared_stack_t *shared_stack = (shared_stack_t *)p;
	printf("f[%x]: starting...\n", pthread_self());
	while (1) {
		//printf("f[%x]: waiting for lock\n", pthread_self());
		rc = pthread_rwlock_rdlock(&shared_stack->mutex);
		printf("f[%x]: got READ lock.\n", pthread_self());
		printf("f[%x]: got READ lock....\n", pthread_self());
        usleep(100000);
		printf("f[%x]: got READ lock.......\n", pthread_self());
		//printf("f[%x]: value=%d\n", pthread_self(), shared_stack->value);
		rc = pthread_rwlock_unlock(&shared_stack->mutex);
        usleep(100000);
	}

}


main() {
	shared_stack_t shared_stack;
	pthread_t thread;
	pthread_attr_t attr;
	int rc;
	/* init shared_stack */
	shared_stack.value = 33;

	rc = pthread_rwlock_init(&shared_stack.mutex, NULL);

	pthread_create(&thread, NULL, &f, &shared_stack);
	pthread_create(&thread, NULL, &f, &shared_stack);
	pthread_create(&thread, NULL, &f, &shared_stack);
    printf("main: sleep(1)...\n");
	sleep(1);
	while (1) {
		rc = pthread_rwlock_wrlock(&shared_stack.mutex);
		printf("main: got WRITE lock.\n");
		usleep(100000);
		printf("main: got WRITE lock...\n");
		shared_stack.value ++;
		printf("main: got WRITE lock......\n");
		printf("main: push value %d (unlock)\n", shared_stack.value);
		rc = pthread_rwlock_unlock(&shared_stack.mutex);
		printf("main: unlock rc=%d\n", rc);
		for (rc=0; rc<10; rc++) printf(".");
		printf("\n");
	}
}
