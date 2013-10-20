#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>
#include <signal.h>

void handle_alarm(int i);

main()
{
	struct itimerval timerval;

	timerval.it_value.tv_sec = 1 ;
	timerval.it_value.tv_usec = 0 ;
	timerval.it_interval = timerval.it_value;

	signal(SIGALRM, handle_alarm);
	setitimer(ITIMER_REAL, &timerval, 0);
	while (1) { pause(); }
}
void handle_alarm(int i)
{
	printf("i=%d\n", i);
}
