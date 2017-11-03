#include <stdlib.h>
#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <mqueue.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

#define MQ_MSG_SIZE 100

void usage()
{
	printf("Usage: mq_recv <q-name>\n");
	exit(1);
}

int main(int argc, char **argv)
{
	if (argc != 2) usage();

    const char * qname = argv[1];

	struct mq_attr attr;
	attr.mq_flags = 0;
	attr.mq_maxmsg = 10;
	attr.mq_msgsize = MQ_MSG_SIZE;
	attr.mq_curmsgs = 0;

	mq_unlink(qname); // clean up possibly already existing queue
	
	// Create queue with mq_open in master process (doc):
	

	mqd_t queue = mq_open(qname, O_CREAT|O_RDWR|O_NONBLOCK, 0644, &attr);
	//queue = mq_open(qname, O_RDONLY);

	if (-1 == queue) {
		printf("mq_open error: %s\n", strerror(errno));
		exit(1);
	}

	printf("Pending messages in queue %s: %ld\n", qname, attr.mq_curmsgs);
	int r = mq_getattr(queue, &attr);
	printf("Pending messages in queue %s: %ld\n", qname, attr.mq_curmsgs);
	
	// In reader process open queue for reading:
	char rcvmsg[MQ_MSG_SIZE];

	while (1) {
		// prepare 'select'
		fd_set rd;
		int nfds = -1;
		FD_ZERO(&rd);
		FD_SET(queue, &rd); // file descriptor
		nfds = queue + 1;

		int status = select(nfds+1, &rd, 0, 0, 0);
		if (status == 0) {
			printf("select returned: %d\n", status);
		} else if (status < 0) {
			if (errno == EINTR) {
				printf("select got: EINTR (interrupted by a signal)\n");
			} else {
				printf("select error: %s\n", strerror(errno));
				exit(1);
			}
		} else {
			if (FD_ISSET(queue, &rd)) {
				int iret = mq_receive(queue, rcvmsg, MQ_MSG_SIZE, 0);
				if (-1 == iret) {
					printf("mq_receive error: %s\n", strerror(errno));
				} else {
					printf("%s: %s\n", qname, rcvmsg);
					if (0 == strcmp(rcvmsg, "quit")) {
						int r = mq_unlink(qname);
						printf("mq_unlink: %d, %s\n", r, strerror(errno));
						exit(0);
					}
				}
				
			} else {
				printf("select indication, but queue not ready\n");
			}
		}
	}
	

}
