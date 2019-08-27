#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#include <sys/poll.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#include <linux/types.h>
#include <linux/netlink.h>

void die(char *s)
{
	write(2, s, strlen(s));
	exit(1);
}

int main(int argc, char *argv[])
{
	struct sockaddr_nl nls;
	struct pollfd pfd;
	char buf[8192];
	int err;

	// Open hotplug event netlink socket

	memset(&nls, 0, sizeof(struct sockaddr_nl));
	nls.nl_family = AF_NETLINK;
	nls.nl_pid = 0; // le t the kernel assign it //getpid();
	nls.nl_groups = -1;

	pfd.events = POLLIN;
	pfd.fd = socket(PF_NETLINK, SOCK_DGRAM, NETLINK_KOBJECT_UEVENT);
	if (pfd.fd==-1) {
		perror("socket error");
		exit(1);
	}

	// Listen to netlink socket

	err = bind(pfd.fd, (void *)&nls, sizeof(struct sockaddr_nl));
	if (err) {
		perror("bind error");
		exit(1);
	}

	while (1) {
		err = poll(&pfd, 1, -1);
	   	if (-1 == err) {
			perror("poll error");
			exit(1);
		}

		int n = recv(pfd.fd, buf, sizeof(buf), MSG_DONTWAIT);
		if (n == -1) {
			perror("recv error");
			exit(1);
		}

		printf("n=%d\n", n);
		// Print the data to stdout.
		int i = 0;
		while (i < n) {
			printf("%s\n", buf+i);
			i += strlen(buf+i)+1;
		}
		printf("--------------------------------------------------------------------------------\n");
	}
	return 0;
}
