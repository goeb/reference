
// warning: mq_receive not working!! (the rest is ok)

/*
 * gcc -lrt mqueue.c
 */

#include <stdlib.h>

#include <string.h>
#include <errno.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>           /* For O_* constants */
#include <sys/stat.h>        /* For mode constants */
#include <mqueue.h>

int main() 
{

	mode_t mode = 0666;
	struct mq_attr attr;
	attr.mq_flags = 0;
	attr.mq_maxmsg = 20;
	attr.mq_msgsize = 50;
	attr.mq_curmsgs = 0;

	//mqd_t q = mq_open("totoqueue", O_CREAT | O_RDWR, mode, &attr);
	mqd_t q = mq_open("/totoqueue", O_RDWR | O_CREAT, 0666, NULL);


	if (q < 0) {
		printf("mq_open error %d: %s\n", q, strerror(errno));
		exit(1);
	}
	
	pid_t x = fork();
	if (x==0) {
		printf("child: ok\n");
		// child
		printf("child sending toto\n");
		int n = mq_send(q, "toto\n", 5, 0);
		if (n<0) printf("mq_send error: %s\n", strerror(errno));
		else printf("mq_send ok\n");
		printf("child: ");	
	} else {
		printf("parent: ok\n");
		// parent
		char buffer[50];
		int n = mq_receive(q, buffer, 50, 0);
		if (n<0) printf("mq_receive error: %s\n", strerror(errno));
		else printf("mq_receive: n=%d\n");
		printf("parent: ");	
	}
	printf("end\n");
	return 0;
}
