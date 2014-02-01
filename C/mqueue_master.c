       #include <fcntl.h>           /* For O_* constants */
       #include <sys/stat.h>        /* For mode constants */
       #include <mqueue.h>
#include <stdio.h>

main()
{
    const char * qname = "/xxx";

	struct mq_attr attr;  
	attr.mq_flags = 0;  
	attr.mq_maxmsg = 10;  
	attr.mq_msgsize = 33;  
	attr.mq_curmsgs = 0;  
	
	// Create queue with mq_open in master process (doc):
	
	mqd_t queue = mq_open(qname, O_CREAT|O_RDWR, 0644, &attr);

	if (-1 == queue) perror("mq_open: ");
	//queue = mq_open(qname, O_RDONLY);
	
	// In reader process open queue for reading:
	char rcvmsg[50+1];

	while (1) {
		int iret = mq_receive(queue, rcvmsg, 50, 0);

		rcvmsg[50] = 0;
		if (-1 == iret) {
			perror("master error: ");
		} else printf("master got: %s\n", rcvmsg);
		sleep(1);
	}
	

}
