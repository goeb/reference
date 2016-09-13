
/*
 * gcc read_certificat.c -lcrypto
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#include <openssl/pem.h>
#include <openssl/x509v3.h>

int main(int argc, char **argv)
{

	X509 x509;
	FILE *fp;
   
	const char *file = argv[1];
	fp	= fopen(file, "r");
	if (NULL == fp) {
		printf("Cannot open file '%s': %s\n", file, strerror(errno));
		exit(1);
	}

	X509 *x = PEM_read_X509(fp, NULL, NULL, NULL);

	printf("x=%p\n", x);
	printf("notBefore=%s\n", x->cert_info->validity->notBefore->data);
	printf("notAfter=%s\n", x->cert_info->validity->notAfter->data);

}
