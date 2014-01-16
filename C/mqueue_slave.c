#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <mqueue.h>
#include <stdio.h>
#include <string.h>

main()
{
	const char * qname = "/xxx";

	struct mq_attr attr;  
	attr.mq_flags = 0;  
	attr.mq_maxmsg = 10;  
	attr.mq_msgsize = 33;  
	attr.mq_curmsgs = 0;  
	
	// open queue for writing:
	mqd_t queue = mq_open(qname, O_WRONLY);
	char buf[100];
	sprintf(buf, "some message from=%d", getpid());
	mq_send(queue, buf, strlen(buf)+1, 1);
	
}
