
#include <errno.h>
#include <string.h>
#include <stdio.h>
#include <termios.h>
#include <unistd.h>
       #include <sys/types.h>
       #include <sys/stat.h>
       #include <fcntl.h>


/* usage:
 * tcdrain <device> <nBytes>
 * example: ./a.out /dev/ttyUSB0 1000
 */

/* set a low speed
 * stty -F /dev/ttyUSB0 ospeed 1200
 * it should take ~ 5.6s to send 841 bytes
 */

int main(int argc, char ** argv) {
	const char * device = argv[1];
	int nBytes = atoi(argv[2]);
	printf("nBytes=%d\n", nBytes);

	int flags = 0;

	// Port Serie
	struct termios term_attr;

	int fd = open(device, O_RDWR | O_NOCTTY | O_NDELAY, 0);
	if (fd  == -1) {
		printf("Failed to open serial connection with plc modem");
		return -1;
	}
	if (tcgetattr(fd, &term_attr) != 0){
		printf("serial connection with plc modem : tcgetattr() failed");
		return -1;
	}

	term_attr.c_cflag = B1200 | CS8 | CLOCAL | CREAD;
	term_attr.c_iflag = IGNPAR;
	term_attr.c_oflag = 0;
	term_attr.c_cflag &= ~CSTOPB;
	term_attr.c_lflag = 0;

	if (tcsetattr(fd, TCSANOW, &term_attr) != 0){
		printf("serial connection with plc modem : tcsetattr() failed");
		return -1;
	}

	if ((flags = fcntl(fd, F_SETFL, FNDELAY)) == -1){
		printf("Failed to set serial connection with plc modem as non-blocking");
		return -1;
	}

	char buf[4096+1];
	while (1) {
		int n = read(fd, buf, 4096);
		if (-1 == n) {
			printf("read error: %s\n", strerror(errno));
			usleep(500000);
		} else {
			buf[n] = 0;
			printf("n=%d: %s\n", n, buf);
		}
		
	}
	return 0;
}
