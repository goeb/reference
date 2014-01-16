/*
    gcc -o threads threads.c -l pthread
*/

/* Server code in C */
 
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/tcp.h>

#include <pthread.h>
#include <signal.h>

 
void * handle(void * param)
{
    int i = *(int *)param;
    printf("thread[%d] handle starting...\n", i);
    printf("thread[%d] closing...\n", i);

    pthread_detach(pthread_self());

}

#define MESSAGING_MGR_THREAD_SIZE 2*1024*1024
#define N_MAX 2000
int main(void)
{
    int i = 0;
    pthread_t table[N_MAX];
    for(i=0; i<N_MAX; i++)
    {
        printf("launching thread [%d]...\n", i);
        pthread_t iThread;
        pthread_attr_t attr;
        pthread_attr_init(&attr);
        //pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);
        pthread_attr_setstacksize(&attr, MESSAGING_MGR_THREAD_SIZE);

        int x = pthread_create(&iThread, &attr, handle, &i);
        printf("pthread_create[%d]: x=%d, errno=%d\n", i, x, errno);
        if (x==0) table[i] = iThread;
        else table[i] = 0;
    }
    for(i=0; i<N_MAX; i++)
    {
        if (table[i])
        {
            int status = pthread_join(table[i], 0);
            printf("pthread_join[%d] returned: %d\n", i, status);
        }
    }
}
