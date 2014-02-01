
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdio.h>

int main() 
{
    int sock = socket(AF_INET, SOCK_STREAM, 0);
	close(sock);
	printf("done.\n");
}
