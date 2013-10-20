
// this tests the synchronisation between 2 threads
//

/* 
 * gcc pthread_cond_signal.c -lpthread
 **/

#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

typedef struct {
	int value;
	pthread_mutex_t mutex;
	pthread_cond_t condition;
	int semCount;
} sem_private_struct, *sem_private;


void * f(void *p) {
	int rc;
	sem_private token = (sem_private)p;
	printf("f: starting...\n");
	while (1) {
		if (rc = pthread_mutex_lock(&(token->mutex))) exit(10);
		printf("f: waiting for lock\n");
		rc = pthread_cond_wait(&(token->condition), &(token->mutex));
		if (rc) exit(11);
		token->semCount--;

		printf("f: value=%d\n", token->value);
		printf("f: semCount=%d\n", token->semCount);
		if (rc = pthread_mutex_unlock(&(token->mutex))) exit(12);
	}

}


main() {
	sem_private token;
	token = (sem_private) malloc(sizeof(sem_private_struct));
	int rc;

	if(rc = pthread_mutex_init(&(token->mutex), NULL)){
		free(token);
		exit(1);
	}

	if(rc = pthread_cond_init(&(token->condition), NULL)) {
		pthread_mutex_destroy( &(token->mutex) );
		free(token);
		exit(2);
	}
	token->semCount = 0;
	pthread_t thread;
	pthread_attr_t attr;

	token->value = 33;

	pthread_create(&thread, NULL, &f, token);
	while (1) {
		printf("main: sleeping 2...\n");
		sleep(2);
		if (rc = pthread_mutex_lock(&(token->mutex))) exit(3);
		token->value ++;
		printf("main: value=%d\n", token->value);
		token->semCount ++;
		if (rc = pthread_mutex_unlock(&(token->mutex))) exit(4);

		// semaphore post
		if (rc = pthread_cond_signal(&(token->condition))) exit(5);
	}
}
