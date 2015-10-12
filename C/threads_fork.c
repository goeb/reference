
/*
 * Test if several system calls launched by several thread
 * do not mess up.
 * 
 * gcc threads.c -lpthread
 *
 **/

#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>



#define MAX_THREADS 5

int ThreadTable[MAX_THREADS] = { 0, 1, 2, 3, 4 };
pthread_t Threads[MAX_THREADS];

void usage(const char *progname)
{
	printf("Usage: %s N_THREADS\n", progname);
	printf("N_THREADS must be <= 5\n");
	exit(1);
}

/* main function of the threads */
void * f(void *p) {
	int threadIndex = *(int*)p;
	int duration = threadIndex + 1;

    pid_t pid = fork();
	/* warning: using hereafter printf, which is not async-safe */
    if (-1 == pid) {
        perror("fork");
        exit(1);
    } else if (pid) {
		/* parent */
		// sleep a while longer than the child in order to get the SIGCHLD
		printf("f[%d]: parent sleeping %d...\n", threadIndex, duration+1);
		sleep(duration+1);
		printf("f[%d]: parent ended.\n", threadIndex);
	} else {
		/* child */
		printf("f[%d]: child sleeping %d...\n", threadIndex, duration);
		sleep(duration);
		printf("f[%d]: child ended.\n", threadIndex);
	}
}


int main(int argc, char **argv)
{
	if (argc < 2) usage(argv[0]);

	const int nThreads = atoi(argv[1]);
	
	if (nThreads > MAX_THREADS) usage(argv[0]);

	int i;
	/* Launch n threads */
	for (i=0; i<nThreads; i++) {
		pthread_create(&Threads[i], NULL, &f, &ThreadTable[i]);
	}

	sleep(nThreads);

	/* Wait for all threads */
	for (i=0; i<nThreads; i++) {
		void *res;
		int r = pthread_join(Threads[i], &res);
		printf("pthread_join(%d): r=%d\n", i, r);
	}
}
