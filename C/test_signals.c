/*
 gcc -o test_signal test_signals.c -lpthread
 */
#include <stdio.h>
#include <pthread.h>
#include <signal.h>

void *thread2(void *x)
{
    sigset_t signal_set;
    int sig;
    while (1)
    {
        printf("thread2: sigwait...\n");
        sigfillset( &signal_set );
        sigwait( &signal_set, &sig );
        printf("thread2: signal received %d\n", sig);
    }
}

void *thread1(void *x)
{
    sigset_t signal_set;
    int sig;
    while (1)
    {
        printf("thread1: sigwait...\n");
        sigfillset( &signal_set );
        sigwait( &signal_set, &sig );
        printf("thread1: signal received %d\n", sig);
        printf("thread1: sleeping 5...\n");
        sleep(5);
    }
}

int main() 
{
    sigset_t signal_set;
    int sig;
    size_t plcstacksize = 1024*1024;

    sigset_t sigmask;
    sigfillset(&sigmask);
    int status = pthread_sigmask(SIG_BLOCK, &sigmask, 0);
    printf("pthread_sigmask: %d\n", status);
    
    pthread_t iThread;
    pthread_attr_t attr;
    pthread_attr_init(&attr);
    pthread_attr_setstacksize (&attr, plcstacksize);

    pthread_create(&iThread, &attr, thread1, NULL);
    //pthread_create(&iThread, &attr, thread2, NULL);


    while (1)
    {
        sleep(1);
        //printf("main: sigwait...\n");
        //sigfillset(&signal_set);
        //sigwait(&signal_set, &sig);
        //printf("main: signal received\n");
    }
}
