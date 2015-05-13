#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <linux/rtnetlink.h>
#include <sys/socket.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <net/if.h>

/* Example of listening to netlink events
 */


void readNetlinkEvent(int sockId)
{
	int status;
	int ret = 0;
	char buf[4096];
	struct iovec iov = { buf, sizeof buf };
	struct sockaddr_nl snl;
	struct msghdr msg = { (void *) &snl, sizeof snl, &iov, 1, NULL, 0, 0 };
	struct nlmsghdr *h;
	struct ifinfomsg *ifi;
	struct ifaddrmsg *ifa;

	status = recvmsg(sockId, &msg, 0);
	if (status < 0) {
		printf("recvmsg error: %s\n", strerror(errno));
		return;
	}

	if (status == 0) {
		printf("recvmsg returned 0\n");
		return;
	}

	// handle 1 or several message per 'recvmsg'
	for (h = (struct nlmsghdr *) buf; NLMSG_OK(h, (unsigned int ) status); h = NLMSG_NEXT(h, status)) {

		if (h->nlmsg_type == NLMSG_DONE) {
			printf("h->nlmsg_type == NLMSG_DONE\n");
			return;

		} else if (h->nlmsg_type == NLMSG_ERROR) {
			printf("h->nlmsg_type == NLMSG_ERROR\n");
			return;

		} else if (h->nlmsg_type == RTM_NEWLINK) {
			printf("h->nlmsg_type == RTM_NEWLINK\n");
			ifi = (struct ifinfomsg*) NLMSG_DATA(h);
			char buf[INET6_ADDRSTRLEN];
			const char *itf = if_indextoname(ifi->ifi_index, buf);
			if (!itf) printf("itf=(nil)\n");
			else printf("itf=%s\n", itf);

			if (ifi->ifi_flags & IFF_UP) {
				printf("IFF_UP\n");
				printf("ifi->ifi_flags & IFF_RUNNING=%d\n", ifi->ifi_flags & IFF_RUNNING);
			} else {
				printf("~IFF_UP (down?)\n");
			}

		} else if (h->nlmsg_type == RTM_NEWADDR) {
			printf("h->nlmsg_type == RTM_NEWADDR\n");
			struct rtattr *rth;
			int rtl;

			ifa = (struct ifaddrmsg*) NLMSG_DATA(h);
			rth = IFA_RTA(ifa);
			rtl = IFA_PAYLOAD(h);

			if (ifa->ifa_family == AF_INET) {

				for (; RTA_OK(rth, rtl); rth = RTA_NEXT(rth, rtl)) {
					char name[IFNAMSIZ];
					char ipaddr[INET_ADDRSTRLEN];

					if (rth->rta_type != IFA_ADDRESS) {
						printf("rth->rta_type != IFA_ADDRESS\n");
						 continue;
					}

					inet_ntop(ifa->ifa_family, RTA_DATA(rth), ipaddr, sizeof(ipaddr));
					printf("ipaddr=%s\n", ipaddr);
				}
			}
		} else if (h->nlmsg_type == RTM_DELADDR) {
			printf("h->nlmsg_type == RTM_DELADDR\n");
			struct rtattr *rth;
			int rtl;

			ifa = (struct ifaddrmsg*) NLMSG_DATA(h);
			rth = IFA_RTA(ifa);
			rtl = IFA_PAYLOAD(h);

			if (ifa->ifa_family == AF_INET) {
				for (; RTA_OK(rth, rtl); rth = RTA_NEXT(rth, rtl)) {
					char name[IFNAMSIZ];
					char ipaddr[INET6_ADDRSTRLEN];

					if (rth->rta_type != IFA_ADDRESS) {
						printf("rth->rta_type != IFA_ADDRESS\n");
						continue;
					}

					inet_ntop(ifa->ifa_family, RTA_DATA(rth), ipaddr, sizeof(ipaddr));
					printf("deleted ipaddr=%s\n", ipaddr);
				}
			}
		} else {
			printf("Got h->nlmsg_type=%d\n", h->nlmsg_type);
		}
	}
}

int main(int argc, char **argv)
{

	int fd = socket(AF_NETLINK, SOCK_RAW, NETLINK_ROUTE);
	if (fd < 0) {
		printf("socket error: %s\n", strerror(errno));
		return 1;
	}

	struct sockaddr_nl addr;
	bzero(&addr, sizeof(addr));

	addr.nl_family = AF_NETLINK;
	addr.nl_pid = getpid();
	addr.nl_groups = RTMGRP_LINK | RTMGRP_IPV4_IFADDR | RTMGRP_IPV6_IFADDR;
	
	if (bind(fd, (struct sockaddr *) &addr, sizeof(addr)) < 0) {
		printf("bind error: %s\n", strerror(errno));
		return 1;
	}

	while (1) {
		int maxFd = -1;
		fd_set readFdMask;
		FD_ZERO(&readFdMask);
		FD_SET(fd, &readFdMask);
		maxFd = fd;
		int r = select(maxFd+1, &readFdMask, 0, 0, 0);
		if (r == -1) {
			printf("select error: %s\n", strerror(errno));
			return 1;
		} else {
			// got event on fd
			readNetlinkEvent(fd);
		}
	}
	return 0;
}

