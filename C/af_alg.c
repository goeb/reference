
/*
 * Example of using the kernel crypto API for computing a sha1
 *
 * Usage:
 *   gcc -o af_alg af_alg.c
 *   ./af_alg hello
 *   send: n=5
 *   read: n=20
 *   sha1: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
 *
 * Verification:
 *   echo -n hello | sha1sum
 *   aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d  -
 * 
 */  

#include <linux/if_alg.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

void hexlify(unsigned char *data, size_t length)
{
	size_t i;
	for (i=0; i<length; i++) {
		printf("%02x", data[i]);
	}
	printf("\n");
}

int main(int argc, char **argv)
{
	if (argc != 2) {
		fprintf(stderr, "Usage: af_alg STRING\n");
		return 1;
	}

	int err, n;
	struct sockaddr_alg sa = {
		.salg_family = AF_ALG,
		.salg_type = "hash",
		.salg_name = "sha1"
	};

	int sock = socket(AF_ALG, SOCK_SEQPACKET, 0);
	err = bind(sock, (struct sockaddr *)&sa, sizeof(sa));
	int worksock = accept(sock, NULL, 0);

	n = send(worksock, argv[1], strlen(argv[1]), 0);
	printf("send: n=%d\n", n);

	unsigned char sha1[20];
	n = read(worksock, sha1, sizeof(sha1));
	printf("read: n=%d\n", n);
	printf("sha1: ");
	hexlify(sha1,  sizeof(sha1));

	return 0;
}
