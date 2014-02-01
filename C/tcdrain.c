
#include <stdio.h>
#include <termios.h>
#include <unistd.h>
       #include <sys/types.h>
       #include <sys/stat.h>
       #include <fcntl.h>


/* usage:
 * tcdrain <device> <nBytes>
 * example: ./a.out /dev/ttyUSB0 1000

 * To be used togeter with tcdrain_listen.c
 */

/* set a low speed
 * stty -F /dev/ttyUSB0 ospeed 1200
 * it should take ~ 5.6s to send 841 bytes
 */

int main(int argc, char ** argv) {
	const char * device = argv[1];
	int nBytes = atoi(argv[2]);
	int doTcdrain = 1;
	if ( (argc>3) ) {
		if (0 == strcmp(argv[3], "--no-tcdrain")) {
			doTcdrain = 0;
		}
	}
	printf("argc=%d, nBytes=%d, doTcdrain=%d\n", argc, nBytes, doTcdrain);

	int flags = 0;

	// Port Serie
	struct termios term_attr;

	int fd = open(device, O_RDWR | O_NOCTTY | O_NDELAY, 0);
	if (fd  == -1) {
		printf("Failed to open serial connection with plc modem\n");
		return -1;
	}
	if (tcgetattr(fd, &term_attr) != 0){
		printf("serial connection with plc modem : tcgetattr() failed\n");
		return -1;
	}

	term_attr.c_cflag = B1200 | CS8 | CLOCAL | CREAD;
	term_attr.c_iflag = IGNPAR;
	term_attr.c_oflag = 0;
	term_attr.c_cflag &= ~CSTOPB;
	term_attr.c_lflag = 0;

	if (tcsetattr(fd, TCSANOW, &term_attr) != 0){
		printf("serial connection with plc modem : tcsetattr() failed\n");
		return -1;
	}

	if ((flags = fcntl(fd, F_SETFL, FNDELAY)) == -1){
		printf("Failed to set serial connection with plc modem as non-blocking\n");
		return -1;
	}

	int i = 0;
	for (i = 0; i < nBytes; i++) {
		int n = write(fd, "x", 1);
	}

	if (doTcdrain) {
		int r = tcdrain(fd);
		printf("tcdrain: r=%d\n", r);
	} else {
		printf("no tcdrain\n");
	}
	return 0;
}
