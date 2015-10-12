
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

void * f(void *p) {
	int threadIndex = *(int*)p;
	//printf("f[%d]: starting...\n", threadIndex);
	char cmd[100];
	int duration = threadIndex + 1;
	sprintf(cmd, "sleep %d ; exit %d", duration, threadIndex);
	printf("f[%d]: running: %s...\n", threadIndex, cmd);
	int r = system(cmd);
	printf("f[%d]: ended. r=%d\n", threadIndex, WEXITSTATUS(r));
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
