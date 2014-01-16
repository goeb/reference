#include <stdio.h>
#include<string.h>
#include<stdlib.h>
#include <fcntl.h>
#include <sys/file.h>
#include <sys/types.h>          /* See NOTES */
#include <sys/socket.h>
#include  <sys/un.h>
#include <sys/signal.h>


#define LOG(...) { printf("server: "); printf(__VA_ARGS__); }

main(int argc, char **argv)
{
	signal(SIGPIPE, SIG_IGN);

	char *path = "logdev";
	int fd = socket(PF_LOCAL, SOCK_STREAM, 0);
	LOG("fd=%d\n", fd);

	struct sockaddr_un adresse;
	adresse.sun_family = AF_LOCAL;
	strcpy(adresse.sun_path, path);
	int taille_adresse = SUN_LEN(&adresse);

	unlink(path);

	LOG("binding... ");
	int rv = bind(fd, (struct sockaddr *) &adresse, taille_adresse);
	printf("rv=%d\n", rv);
 
	LOG("listen... ");
	rv = listen(fd, 100);
	printf("rv=%d\n", rv);
	
	LOG("unblocking...\n");
    int flags = fcntl(fd, F_GETFL,0);
    fcntl(fd, F_SETFL, flags | O_NDELAY);

	int sleepBeforeStart = atoi(argv[1]);
	LOG("sleeping %d...\n", sleepBeforeStart);
	sleep(sleepBeforeStart);

	do {
		LOG("accepting... ");
		int sock = accept(fd, NULL, NULL);
		printf("sock=%d\n", sock);

		if (sock>0) {
			LOG("reading... ");
			char buf[10];
			int n = read(sock, buf, 10);
			printf("n=%d, buf=%s\n", n, buf);
			LOG("writing ACK...");
			n = write(sock, "ACK", 3);
			printf("n=%d\n", n);
			close(sock);
			sleep(1);
		}
		
		sleep(1);
	} while (1);

	LOG("exiting...\n");
}
