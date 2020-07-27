#include <errno.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/epoll.h>
#include <unistd.h>
#include <string.h>


#define MAX_EVENTS 10

int main()
{
	struct epoll_event ev, events[MAX_EVENTS];
	int listen_sock, conn_sock, nfds, epollfd;
	int n;

	/* Set up listening socket, 'listen_sock' (socket(),
	   bind(), listen()) */
	listen_sock = 0; // stdin

	epollfd = epoll_create(10);
	if (epollfd == -1) {
		perror("epoll_create");
		exit(EXIT_FAILURE);
	}

	ev.events = EPOLLIN;
	ev.data.fd = listen_sock;
	if (epoll_ctl(epollfd, EPOLL_CTL_ADD, listen_sock, &ev) == -1) {
		perror("epoll_ctl: listen_sock");
		exit(EXIT_FAILURE);
	}

	for (;;) {
		nfds = epoll_wait(epollfd, events, MAX_EVENTS, -1);
		printf("epoll_wait: nfds=%d\n", nfds);
		if (nfds == -1 && errno != EINTR) {
			perror("epoll_pwait");
			exit(EXIT_FAILURE);
		}
		if (nfds == 1) {
			// read the first event slot
			char buf[100];
			memset(buf, 0, 100);
			ssize_t n = read(events[0].data.fd, buf, 100);
			printf("got: %s\n", buf);
		}
	}
}
