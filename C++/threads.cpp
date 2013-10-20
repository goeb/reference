
#include <iostream>
using namespace std;
#include <stdlib.h>
#include <pthread.h>

void *my_thread_process (void * arg)
{
  int i;

  for (i = 0 ; i < 15 ; i++) {
    cout << "Thread " << (char*)arg << ": " << i << endl;
    sleep (1);
  }
  pthread_exit (0);
}

main (int ac, char **av)
{
  pthread_t th1, th2;
  void *ret;

  if (pthread_create (&th1, NULL, my_thread_process, (char *)"1") < 0) {
    cerr << "pthread_create error for thread 1\n";
    exit (1);
  }

  if (pthread_create (&th2, NULL, my_thread_process, (char*)"2") < 0) {
    cerr << "pthread_create error for thread 2\n";
    exit (1);
  }

  (void)pthread_join (th1, &ret);
  (void)pthread_join (th2, &ret);
  cout << "done.\n";
}

