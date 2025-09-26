/*
 * Compile with:
 * gcc -o openssl_verify openssl_verify.c -lcrypto
 *
 * Test:
 *
 * Generate a private key:
 *     openssl ecparam -name prime256v1 -genkey -out key-ec-prime256v1-priv.pem
 * Compute the related public key:
 *     openssl ec -in key-ec-prime256v1-priv.pem -pubout -out key-ec-prime256v1-pub.pem
 * Generate a self-signed certificate
 *     openssl req -x509 -key key-ec-prime256v1-priv.pem -out key-ec-prime256v1-cert.pem -subj "/CN=key-ec-prime256v1/" -days 3650
 * Create a message and sign it:
 *     echo hello > msg.txt
 *     openssl dgst -sha256 -sign key-ec-prime256v1-priv.pem -out msg.sig msg.txt 
 *
 * Execute this program:
 *    ./openssl_verify msg.txt key-ec-prime256v1-cert.pem msg.sig
 *    signature verification: success
 *
 * Test with another message:
 *     echo hello2 > msg2.txt
 *     ./openssl_verify msg2.txt key-ec-prime256v1-cert.pem msg.sig
 *     signature verification: failed
 */
#include <openssl/evp.h>
#include <openssl/pem.h>
#include <stdint.h>
#include <stdio.h>

int verify(uint8_t *msg, size_t msg_len, EVP_PKEY *pubkey, uint8_t *sig, size_t sig_len)
{
	int ret = -1; // failure by default

	EVP_MD_CTX *mdctx = EVP_MD_CTX_create();
	int status;

	status = EVP_DigestVerifyInit(mdctx, NULL, EVP_sha256(), NULL, pubkey);
	if (status != 1) goto error;

	status = EVP_DigestVerifyUpdate(mdctx, msg, msg_len);
	if (status != 1) goto error;

	status = EVP_DigestVerifyFinal(mdctx, sig, sig_len);
	if (status != 1) goto error;
 
	ret = 0; // success

error:
	EVP_MD_CTX_destroy(mdctx);
	return ret;
}

int usage()
{
	printf("usage: openssl_verify MESSAGE-FILE PEM-CERTIFICATE SIGNATURE-FILE\n");
	return 1;
}

int main(int argc, char **argv)
{
	if (argc != 4) return usage();

	int exit_code = EXIT_FAILURE;
	FILE *certfile = NULL;
	X509 *x509cert = NULL;

	// Load the message
	uint8_t msg[100]; // max size
	FILE *msgfile = fopen(argv[1], "r");
	if (!msgfile) {
		perror("Cannot open MESSAGE-FILE");
		goto end;
	}
	size_t msg_len = fread(msg, 1, sizeof(msg), msgfile);
	fprintf(stderr, "read %lu bytes from %s\n", msg_len, argv[1]);
	fclose(msgfile);

	// Load the signature
	uint8_t sig[4096]; // max size
	FILE *sigfile = fopen(argv[3], "r");
	if (!sigfile) {
		perror("Cannot open SIGNATURE-FILE");
		goto end;
	}
	size_t sig_len = fread(sig, 1, sizeof(sig), sigfile);
	fprintf(stderr, "read %lu bytes from %s\n", sig_len, argv[3]);
	fclose(sigfile);

	certfile = fopen(argv[2], "r");
	if (!certfile) {
		perror("Cannot open PEM-CERTIFICATE");
		goto end;
	}

	// Load the X509 PEM certificate
	x509cert = PEM_read_X509(certfile, NULL, 0, NULL);
	if (!x509cert) {
		fprintf(stderr, "Cannot load x509 certificate\n");
		fclose(certfile);
		return EXIT_FAILURE;
	}

	// Get the public key
	EVP_PKEY *pubkey = X509_get0_pubkey(x509cert);
	if (!pubkey) {
		fprintf(stderr, "Cannot get public key\n");
		goto end;
	}

	int err = verify(msg, msg_len, pubkey, sig, sig_len);

	if (err) {
		printf("signature verification: failed\n");
	} else {
		printf("signature verification: success\n");
		exit_code = EXIT_SUCCESS;
	}

end:
	if (certfile) fclose(certfile);
	if (x509cert) X509_free(x509cert);
	return exit_code;
}
