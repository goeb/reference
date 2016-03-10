/*
 * gcc timer_create.c -lrt
 */
#include <signal.h>
#include <time.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>

pthread_t t1;

void * thread1(void *p)
{
    printf("thread1: starting...\n");
	sigset_t signal_set;
	int sig;

	while(1) {
		/* wait for any and all signals */
		sigfillset( &signal_set );
		sigwait( &signal_set, &sig );
		printf("thread1: got sig %d\n", sig);
	}

    printf("thread1: ending...\n");
}

void block_signals() {
	int err;
	sigset_t sigmask;

	/* Block all signals so that we handle them in a dedicated thread */
	sigfillset(&sigmask);
	err = pthread_sigmask(SIG_BLOCK, &sigmask, NULL);
	if (err) {
		printf("pthread_sigmask error: %s", err, strerror(errno));
	}
}
void launch_thread() {

	block_signals();
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


void f(sigval_t value)
{
	printf("f()...\n");
}

int main()
{
	struct sigevent event;
	event.sigev_value.sival_ptr = NULL;
	event.sigev_notify = SIGEV_THREAD;
	event.sigev_notify_attributes = NULL;
	event.sigev_notify_function = &f;

	timer_t timer;

	timer_create(CLOCK_MONOTONIC, &event, &timer);
	
	struct itimerspec timer_spec;
	timer_spec.it_interval.tv_sec = 1;
	timer_spec.it_interval.tv_nsec = 0;
	timer_spec.it_value.tv_sec = 1;
	timer_spec.it_value.tv_nsec = 0;
	timer_settime(timer, 0, &timer_spec, NULL);

	launch_thread();
	sleep(5);
	stop_thread();

	printf("timer_delete...\n");
	timer_delete(timer);

	printf("exit 0...\n");
	exit(0);
}
