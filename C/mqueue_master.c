#include <stdlib.h>
#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <mqueue.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

#define MQ_MSG_SIZE 100

main()
{
    const char * qname = "/xxx";

	struct mq_attr attr;  
	attr.mq_flags = 0;  
	attr.mq_maxmsg = 20;  
	attr.mq_msgsize = MQ_MSG_SIZE;  
	attr.mq_curmsgs = 0;  
	
	// Create queue with mq_open in master process (doc):
	
	mqd_t queue = mq_open(qname, O_CREAT|O_RDWR|O_NONBLOCK, 0644, &attr);

	if (-1 == queue) perror("mq_open: ");
	//queue = mq_open(qname, O_RDONLY);
	
	// In reader process open queue for reading:
	char rcvmsg[MQ_MSG_SIZE];

	while (1) {
		struct mq_attr attr;
		int r = mq_getattr(queue, &attr);
		printf("Pending messages in queue: %ld\n", attr.mq_curmsgs);
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
					printf("master got: [%s]\n", rcvmsg);
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
