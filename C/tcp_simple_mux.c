
/* usage example:
 *
 * 1. Terminal-1: ./tcp_simple_mux 8888
 * 2. Terminal-2: curl http://localhost:8888/
 * 3. Terminal-3: curl http://localhost:8888/
 * 4. Terminal-4: curl http://localhost:8888/
 *
 * 5. Terminal-1: Enter the following:
 *     HTTP/1.1 200 OK
 *     Connection: close
 *     Content-Length: 5
 *
 *     toto
 *
 * 6. Terminal-2: gets the answer and terminates.
 *
 * 7. Restart step 5, and the curl clients from steps 3 and 4 will get their answer.
 *
 */
 
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

#include <poll.h>

#include <signal.h>

void usage(const char *progname)
{
	fprintf(stderr, "Usage: %s <port>\n", progname);
	exit(1);
}
 
void handle_connection(int sock)
{
	fprintf(stderr, "hanndle_connection sock=%d\n", sock);

	//const int socketFlag = 1;
	//int err = setsockopt(sock, IPPROTO_TCP, TCP_NODELAY, &socketFlag, sizeof(socketFlag));
	//fprintf(stderr, "setsockopt=%d\n", err);


	// wait for bytes received on the socket or on stdin
	// and forward the bytes from one side to the other

	unsigned char buffer[1024];

	struct pollfd ufds[2];
	ufds[0].fd = 0; // stdin
	ufds[0].events = POLLIN;
	ufds[1].fd = sock;
	ufds[1].events = POLLIN;

	while (1) {
		int rv = poll(ufds, 2, 10000); // 10 second timeout
		if (rv == -1) {
			perror("poll");
			exit(1);
		} else if (rv == 0) {
			fprintf(stderr, "Timeout occurred!\n");
			break;
		}

		if (ufds[0].revents & POLLIN) {
			char buffer[1024];
			int n = read(0, buffer, sizeof buffer);
			fprintf(stderr, "read-stdin: n=%d\n", n);
			if (n < 0) {
				perror("read from stdin");
				exit(1);
			}
			if (n == 0) {
				// stdin closed ?
				fprintf(stderr, "stdin closed?\n");
				exit(1);
			}
			n = write(sock, buffer, n);
			if (n < 0) {
				perror("write to sock");
				exit(1);
			}

		} else if (ufds[1].revents & POLLIN) {
			int n = read(sock, buffer, sizeof buffer);
			fprintf(stderr, "read-sock: n=%d\n", n);
			if (n < 0) {
				perror("read from sock");
				exit(1);
			} 
			if (n == 0) {
				// peer has closed ?
				fprintf(stderr, "peer closed?\n");
				break;
			}
			n = write(1, buffer, n);
			if (n < 0) {
				perror("write to stdout");
				exit(1);
			}
		} else {
			fprintf(stderr, "other: ufds[0].revents=%d, ufds[1].revents=%d\n", ufds[0].revents, ufds[1].revents);
		}
	}
 
	shutdown(sock, SHUT_RDWR);
	close(sock);
	fprintf(stderr, "hanndle_connection completed.\n");
}

int main(int argc, char **argv)
{
	struct sockaddr_in stSockAddr;
	int SocketFD = socket(PF_INET, SOCK_STREAM, 0);
	int socketFlag = 1;

	if (argc != 2) usage(argv[0]);

	int port = atoi(argv[1]);

	setsockopt(SocketFD, SOL_SOCKET, SO_REUSEADDR, &socketFlag, sizeof(socketFlag));

	if(-1 == SocketFD)
	{
		perror("can not create socket");
		exit(EXIT_FAILURE);
	}

	memset(&stSockAddr, 0, sizeof(stSockAddr));

	stSockAddr.sin_family = AF_INET;
	stSockAddr.sin_port = htons(port);
	stSockAddr.sin_addr.s_addr = INADDR_ANY;

	if(-1 == bind(SocketFD,(struct sockaddr *)&stSockAddr, sizeof(stSockAddr)))
	{
		perror("error bind failed");
		close(SocketFD);
		exit(EXIT_FAILURE);
	}

	int i = 0;
	int x = listen(SocketFD, 5);
	printf("listen=%d\n", x);

	while (1)
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

		handle_connection(ConnectFD);
	}
}
