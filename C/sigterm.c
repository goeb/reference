
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <signal.h>

static do_quit = 0;

void sig_handler(int sig)
{
	fprintf(stderr, "entering sigterm_handler: sig=%d\n", sig);
	do_quit = 1;
	sleep(1);
	fprintf(stderr, "exiting sigterm_handler\n", sig);
}

int main()
{
	struct sigaction act;
	int ret;
	act.sa_handler = sig_handler;
	sigemptyset (&act.sa_mask);
	act.sa_flags = 0;

	ret = sigaction(SIGTERM, &act, 0);
	printf("sigaction(SIGTERM): ret=%d, %s\n", ret, strerror(errno));
	ret = sigaction(SIGINT, &act, 0);
	printf("sigaction(SIGINT): ret=%d, %s\n", ret, strerror(errno));

	while (1) {
		sleep(1);
	}
}

