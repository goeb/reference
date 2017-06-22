#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <mqueue.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
	const char *msg = "hello";
	if (argc > 1) msg = argv[1];

	const char * qname = "/xxx";

	// open queue for writing:
	mqd_t queue = mq_open(qname, O_WRONLY|O_NONBLOCK);
	if (queue == -1) {
		printf("mq_open error: %s\n", strerror(errno));
		exit(1);
	}

	struct mq_attr attr;
    int r = mq_getattr(queue, &attr);
    printf("Info on queue: maxmsg=%ld, msgsize=%ld, curmsgs=%ld\n", attr.mq_maxmsg, attr.mq_msgsize, attr.mq_curmsgs);

	r = mq_send(queue, msg, strlen(msg)+1, 1); // take the null terminating char
	if (r != 0) printf("mq_send error: %s\n", strerror(errno));
	
}
