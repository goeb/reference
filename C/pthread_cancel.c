/*
 * gcc timer_create.c -lrt
 */
#include <signal.h>
#include <time.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <pthread.h>


pthread_t t1;

void * thread1(void *p)
{
    printf("thread1: starting...\n");
	int old;
	int r = pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, &old);
	printf("thread1: pthread_setcancelstate=%d\n", r);

	while(1) {
		printf("thread1: ... \n");
		sleep(100);
		printf("thread1: after sleep\n");
	}

    printf("thread1: ending...\n");
}

void launch_thread() {

    pthread_attr_t attr;
    pthread_create(&t1, NULL, &thread1, 0);
}

void stop_thread()
{
	int err = pthread_cancel(t1);
	if (err) {
		printf("pthread_cancel error: %s\n", strerror(err));
		return;
	}

	/* Wait thread termination */
	err = pthread_join(t1, NULL);
	if (err) {
		printf("pthread_join error: %s\n", strerror(err));
		return;
	}

}

int main()
{

	launch_thread();
	sleep(2);
	stop_thread();

	printf("exit 0...\n");
	exit(0);
}
