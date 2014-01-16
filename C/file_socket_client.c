#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/file.h>
#include <sys/types.h>          /* See NOTES */
#include <sys/socket.h>
#include  <sys/un.h>
#include <errno.h>
#include <sys/signal.h>



#define LOG(...) { printf("client: "); printf(__VA_ARGS__); }

main(int argc, char ** argv)
{
	signal(SIGPIPE, SIG_IGN);

	char *path = "logdev";
	int fd = socket(PF_LOCAL, SOCK_STREAM, 0);
	LOG("fd=%d\n", fd);
	struct sockaddr_un adresse;
	adresse.sun_family = AF_LOCAL;
	strcpy(adresse.sun_path, path);
	int taille_adresse = SUN_LEN(&adresse);

	LOG("connecting...\n");
	int rv = connect(fd, (struct sockaddr *) &adresse, taille_adresse);
	LOG("connect: rv=%d, %s\n", rv, strerror(errno));
	
	LOG("unblocking...\n");
    int flags = fcntl(fd, F_GETFL,0);
    fcntl(fd, F_SETFL, flags | O_NDELAY);

	const char *data = "0123456789";
	int i;
	for (i=0; i<atoi(argv[1]); i++) {
		rv = write(fd, data, strlen(data));
		if (rv == -1) {
			printf(" (i=%d)\n", i);
			perror("client: write ");
			break;
		}
		//char buffer[100];
		//rv = read(fd, buffer, 100);
		//if (rv == -1) {
		//	perror("client: read ");
		//}
		printf(".");
		//LOG("write: %s, rv=%d\n", data, rv);
	}

	//sleep(atoi(argv[1]));
	data = "xuxuxu";
	rv = write(fd, data, strlen(data));
	LOG("write: %s, rv=%d\n", data, rv);

	//LOG("connecting (2!!!!)...\n");
	//rv = connect(fd, (struct sockaddr *) &adresse, taille_adresse);
	//LOG("connect: rv2=%d, %s\n", rv, strerror(errno));
	

	close(fd);
	LOG("exiting...\n");
}
