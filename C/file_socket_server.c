#include <stdio.h>
#include<string.h>
#include<stdlib.h>
#include <fcntl.h>
#include <sys/file.h>
#include <sys/types.h>          /* See NOTES */
#include <sys/socket.h>
#include  <sys/un.h>

#define LOG(...) { printf("server: "); printf(__VA_ARGS__); }

main(int argc, char **argv)
{

	char *path = "logdev";
	int fd = socket(PF_LOCAL, SOCK_STREAM, 0);
	LOG("fd=%d\n", fd);

	struct sockaddr_un adresse;
	adresse.sun_family = AF_LOCAL;
	strcpy(adresse.sun_path, path);
	int taille_adresse = SUN_LEN(&adresse);

	unlink(path);

	LOG("binding...\n");
	int rv = bind(fd, (struct sockaddr *) &adresse, taille_adresse);
	LOG("bind: rv=%d\n", rv);
 
	LOG("listen...\n");
	rv = listen(fd, 10);
	LOG("listen: rv=%d\n", rv);
	
	LOG("sleep ing 100...\n");
	sleep(100);

	LOG("unblocking...\n");
    int flags = fcntl(fd, F_GETFL,0);
    fcntl(fd, F_SETFL, flags | O_NDELAY);

	int sleepBeforeStart = atoi(argv[1]);
	LOG("sleeping %d...\n", sleepBeforeStart);
	sleep(sleepBeforeStart);

	do {
		LOG("accepting...\n");
		int sock = accept(fd, NULL, NULL);
		LOG("accept: sock=%d\n", sock);

		if (sock>0) do {
			LOG("reading...\n");
			char buf[10];
			int n = read(sock, buf, 10);
			LOG("read: n=%d, buf=%s\n", n, buf);
			if (n<=0) { close(sock); exit(0);}
		} while (1);
		
		sleep(1);
	} while (1);

	LOG("exiting...\n");
}
