/*
 * gcc timer_create.c -lrt
 */
#include <signal.h>
#include <time.h>
#include <stdio.h>
#include <unistd.h>

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

	sleep(2);

	printf("timer_delete...\n");
	timer_delete(timer);

	sleep(2);

}
