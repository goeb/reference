#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <mqueue.h>
#include <stdio.h>
#include <string.h>

void usage()
{
	printf("Usage: mqueue_send <q-name> [<msg>]\n");
	exit(1);
}

int main(int argc, char **argv)
{
	if (argc <= 1 || argc > 3) usage();

	const char *qname = argv[1];
	const char *msg = NULL;
	if (argc == 3) msg = argv[2];

	// open queue for writing:
	mqd_t queue = mq_open(qname, O_WRONLY|O_NONBLOCK);
	if (queue == -1) {
		printf("mq_open error: %s\n", strerror(errno));
		exit(1);
	}

	if (msg) {
		int ret = mq_send(queue, msg, strlen(msg)+1, 1); // take the null terminating char
		if (ret != 0) printf("mq_send error: %s\n", strerror(errno));

	} else {
		struct mq_attr attr;
    	int ret = mq_getattr(queue, &attr);
		if (ret != 0) printf("mq_send error: %s\n", strerror(errno));
		else printf("mq[%s]: maxmsg=%ld, msgsize=%ld, curmsgs=%ld\n", 
				qname, attr.mq_maxmsg, attr.mq_msgsize, attr.mq_curmsgs);
	}
	
}
