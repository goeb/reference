
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
    printf("thread handle starting...\n");
    int SocketFD = *(int*)param;
    const int socketFlag = 1;
    int x = setsockopt(SocketFD, IPPROTO_TCP, TCP_NODELAY, &socketFlag, sizeof(socketFlag));
    printf("setsockopt=%d\n", x);

    unsigned char buff[1024];
    int n = recv(SocketFD, buff, 1024, MSG_DONTWAIT);
    printf("%d bytes received. errno=%d\n", n, errno);
 
    shutdown(SocketFD, SHUT_RDWR);
 
    close(SocketFD);
    printf("thread closing...\n");
}

int main(void)
{
  struct sockaddr_in stSockAddr;
  int SocketFD = socket(PF_INET, SOCK_STREAM, 0);
  int socketFlag = 1;
  setsockopt(SocketFD, SOL_SOCKET, SO_REUSEADDR, &socketFlag, sizeof(socketFlag));
 
  if(-1 == SocketFD)
  {
    perror("can not create socket");
    exit(EXIT_FAILURE);
  }
 
  memset(&stSockAddr, 0, sizeof(stSockAddr));
 
  stSockAddr.sin_family = AF_INET;
  stSockAddr.sin_port = htons(9999);
  stSockAddr.sin_addr.s_addr = INADDR_ANY;
 
  if(-1 == bind(SocketFD,(struct sockaddr *)&stSockAddr, sizeof(stSockAddr)))
  {
    perror("error bind failed");
    close(SocketFD);
    exit(EXIT_FAILURE);
  }
 
    int i = 0;

// test if several listen may leak memory
int N = 1000000;
int x;	
fprintf(stderr, "while(i<N) listen() , N=%d...\n", N);
while (i<N) {
	x = listen(SocketFD, 5);
	i++;
}
    fprintf(stderr, "done.");

	i = 0;
  for(;;)
  {
    printf("accepting...\n");
    int ConnectFD = accept(SocketFD, NULL, NULL);
    printf("accept : ConnectFD=%d\n", ConnectFD);
 
    if(0 > ConnectFD)
    {
      perror("error accept failed");
      close(SocketFD);
      exit(EXIT_FAILURE);
    }
 
    printf("Connection accepted [%d].\n", i);
    i++ ;

    pthread_t iThread;
    pthread_attr_t attr;
    pthread_attr_init(&attr);

    int x = pthread_create(&iThread, &attr, handle, &ConnectFD);
    printf("pthread_create: x=%d\n", x);

    //handle(&ConnectFD);
  }
}
