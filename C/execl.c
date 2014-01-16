
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>

int main() {

	const char *cmd = "cpin=0000 mtu=1000 mru=1000 apn=BTAWL-Linky login=noctestbouygues01@nocapn02.fr.fg pwd=edisflz1 phone=*99***1# pppd nodetach defaultroute local lock /dev/ttyS1 user noctestbouygues01@nocapn02.fr.fg password edisflz1 mru 1000 mtu 1000 connect 'chat -s -E -f /etc/ppp/peers/gprs_connect.txt'";

	pid_t p = vfork(); // use vfork to be sure that
	if (p > 0) {
		// in parent
		printf("vfork/parent: p=%d", p);
	} else if (p == -1) {
		// error
		printf("vfork error: %s", strerror(errno));
	} else {
		// in child

		int r = execl("/bin/sh", "/bin/sh", "-c", cmd, NULL);
		printf("r/execl=%d\n", r);
	}
	printf("parent done\n");
}
