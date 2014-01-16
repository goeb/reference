#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
int main(int argc, char** argv)
{
	int bytesWritten = 0;
	int i = 15;
	int f = open("myfifo", O_WRONLY | O_APPEND | O_NONBLOCK);
	if (f < 0) {
		perror("Cannot open");
		return 1;
	} else fprintf(stderr, "open: ok\n");

	sleep(1);

	while (i) {
		char buffer[1000];
		sprintf(buffer, "2012-07-05 14:42:47.016 DEBUG   txt-000102030405060708090A0B0C0D0E0F-AAAA-EEEE, i=%d\n", i);
		int n = write(f, buffer, strlen(buffer));
		fprintf(stderr, "write: n=%d, i=%d, bytesWritten=%d\n", n, i, bytesWritten);
		if (n < 0) {
			perror("Cannot write");
		} else {
			i--;
			bytesWritten += n;
		}
		usleep(10000); // 10 ms
	}
	close(f);

	fprintf(stderr, "end.\n");
	return 0;
}
