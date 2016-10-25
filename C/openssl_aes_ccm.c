#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>


#define handleErrors() fprintf(stderr, "error:%s:%d\n", __FILE__, __LINE__);

int encryptccm(const unsigned char *plaintext, int plaintext_len, const unsigned char *aad,
	int aad_len, const unsigned char *key, const unsigned char *iv,
	unsigned char *ciphertext, unsigned char *tag)
{
	EVP_CIPHER_CTX *ctx;

	int len;
	int ciphertext_len;

	/* Create and initialise the context */
	if(!(ctx = EVP_CIPHER_CTX_new())) handleErrors();

	/* Initialise the encryption operation. */
	if(1 != EVP_EncryptInit_ex(ctx, EVP_aes_128_ccm(), NULL, NULL, NULL)) handleErrors();

	/* Setting IV len to 7. Not strictly necessary as this is the default
	 * but shown here for the purposes of this example */
	if(1 != EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_CCM_SET_IVLEN, 7, NULL)) handleErrors();

	/* Set tag length */
	EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_CCM_SET_TAG, 14, NULL);

	/* Initialise key and IV */
	if(1 != EVP_EncryptInit_ex(ctx, NULL, NULL, key, iv)) handleErrors();

	/* Provide the total plaintext length */
	if(1 != EVP_EncryptUpdate(ctx, NULL, &len, NULL, plaintext_len)) handleErrors();

	/* Provide any AAD data. This can be called zero or one times as * required */
	if(1 != EVP_EncryptUpdate(ctx, NULL, &len, aad, aad_len)) handleErrors();

	/* Provide the message to be encrypted, and obtain the encrypted output.
	 * EVP_EncryptUpdate can only be called once for this
	 */
	if(1 != EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len)) handleErrors();
	ciphertext_len = len;

	/* Finalise the encryption. Normally ciphertext bytes may be written at
	 * this stage, but this does not occur in CCM mode
	 */
	if(1 != EVP_EncryptFinal_ex(ctx, ciphertext + len, &len)) handleErrors();
	ciphertext_len += len;

	/* Get the tag */
	if(1 != EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_CCM_GET_TAG, 14, tag)) handleErrors();

	/* Clean up */
	EVP_CIPHER_CTX_free(ctx);

	return ciphertext_len;
}

int decryptccm(const unsigned char *ciphertext, int ciphertext_len, const unsigned char *aad,
	int aad_len, unsigned char *tag, const unsigned char *key, const unsigned char *iv,
	unsigned char *plaintext)
{
	EVP_CIPHER_CTX *ctx;
	int len;
	int plaintext_len;
	int ret;

	/* Create and initialise the context */
	if(!(ctx = EVP_CIPHER_CTX_new())) handleErrors();

	/* Initialise the decryption operation. */
	if(1 != EVP_DecryptInit_ex(ctx, EVP_aes_128_ccm(), NULL, NULL, NULL)) handleErrors();

	/* Setting IV len to 7. Not strictly necessary as this is the default
	 * but shown here for the purposes of this example */
	if(1 != EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_CCM_SET_IVLEN, 7, NULL)) handleErrors();

	/* Set expected tag value. */
	if(1 != EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_CCM_SET_TAG, 14, tag)) handleErrors();

	/* Initialise key and IV */
	if(1 != EVP_DecryptInit_ex(ctx, NULL, NULL, key, iv)) handleErrors();

	/* Provide the total ciphertext length
	 */
	if(1 != EVP_DecryptUpdate(ctx, NULL, &len, NULL, ciphertext_len)) handleErrors();

	/* Provide any AAD data. This can be called zero or more times as
	 * required
	 */
	if(1 != EVP_DecryptUpdate(ctx, NULL, &len, aad, aad_len)) handleErrors();

	/* Provide the message to be decrypted, and obtain the plaintext output.
	 * EVP_DecryptUpdate can be called multiple times if necessary
	 */
	ret = EVP_DecryptUpdate(ctx, plaintext, &len, ciphertext, ciphertext_len);

	plaintext_len = len;

	/* Clean up */
	EVP_CIPHER_CTX_free(ctx);

	if(ret > 0)
	{
		/* Success */
		return plaintext_len;
	}
	else
	{
		/* Verify failed */
		return -1;
	}
}


const char *printhex(const char *prefix, const unsigned char *data, int len)
{
	printf("%s", prefix);
	int i;
	for (i=0; i<len; i++) {
		printf("%02x", data[i]);
	}
	printf("\n");
}

int main(int argc, char **argv)
{
	const char *plaintext = "hello world!";
	unsigned char *aad = "zzzz";
	unsigned char *key = "0123456789abcdef";
	unsigned char *iv = "3333333333333333";
	const int SIZ=50;
	unsigned char ciphertext[SIZ];
	unsigned char tag[SIZ];
	memset(ciphertext, 0, SIZ);
	memset(tag, 0, SIZ);

	int err = encryptccm(plaintext, strlen(plaintext), aad, sizeof(aad), key, iv, ciphertext, tag);

	printf("encrypt-err=%d\n", err);
	printhex("ciphertext=", ciphertext, SIZ);
	printhex("tag=", tag, SIZ);

	// now decrypt
	
	char decrypted[SIZ];
	memset(decrypted, 0, SIZ);
	err = decryptccm(ciphertext, strlen(plaintext), aad, sizeof(aad), tag, key, iv, decrypted);

	printf("decrypt-err=%d\n", err);
	printf("decrypted=%s\n", decrypted);
}
