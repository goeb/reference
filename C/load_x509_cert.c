
/* 
 * Print information of a x509 certificate
 *
 * Example:
 * $ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"
 * $ gcc -o load_x509_cert load_x509_cert.c -l crypto
 * $ ./load_x509_cert cert.pem 
 * issuer: /C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname
 * subject: /C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname
 * 2025-01-04 14:19:49Z
 * 2035-01-02 14:19:49Z
 * Subject Public Key Info:
 * Public Public Key Algorithm: rsaEncryption
 * X509_verify: 1, Signature ok
 * Subject key id: EE5678837CBF5D942D231788D395370BE54723CC
 * Authority key id: EE5678837CBF5D942D231788D395370BE54723CC
 * 
 */
#include <stdio.h>
#include <openssl/asn1.h>
#include <openssl/pem.h>
#include <openssl/x509.h>
#include <openssl/x509v3.h>

void hexdump(BIO *out, unsigned char *data, int length) {
	for (int i = 0; i < length; i++) {
        int err = BIO_printf(out, "%02X", data[i]);
		if (err <= 0) return;
   	}
}

int main(int argc, char **argv)
{
	int err;
	char buffer[4096];
	BIO *out;
	out = BIO_new_fd(fileno(stdout), BIO_NOCLOSE);

	FILE *certfile = fopen(argv[1], "r");
	X509 *x509cert = PEM_read_X509(certfile, NULL, 0, NULL);

	X509_NAME *issuer = X509_get_issuer_name(x509cert);
	char *issuer_str  = X509_NAME_oneline(issuer, buffer, sizeof(buffer));
	BIO_printf(out, "issuer: %s\n", issuer_str);

	//ASN1_INTEGER *X509_get_serialNumber(x509cert);
	
	X509_NAME *subject = X509_get_subject_name(x509cert);
	char *subject_str  = X509_NAME_oneline(subject, buffer, sizeof(buffer));
	BIO_printf(out, "subject: %s\n", subject_str);

	ASN1_TIME *not_before = X509_getm_notBefore(x509cert);
	ASN1_TIME_print_ex(out, not_before, ASN1_DTFLGS_ISO8601);
	BIO_printf(out, "\n");

	ASN1_TIME *not_after = X509_getm_notAfter(x509cert);
	ASN1_TIME_print_ex(out, not_after, ASN1_DTFLGS_ISO8601);
	BIO_printf(out, "\n");

	X509_PUBKEY *xpkey = X509_get_X509_PUBKEY(x509cert);
	ASN1_OBJECT *xpoid;
	X509_PUBKEY_get0_param(&xpoid, NULL, NULL, NULL, xpkey);
	BIO_write(out, "Subject Public Key Info:\n", 33);
	BIO_printf(out, "Public Key Algorithm: ");
	i2a_ASN1_OBJECT(out, xpoid);
	BIO_puts(out, "\n");

	EVP_PKEY *pubkey = X509_get0_pubkey(x509cert);
	if (!pubkey) {
		BIO_printf(out, "error in X509_get0_pubkey\n");
		return 1;
	}

	// Check the cert signature with its own public key (is self-signed?)
    err = X509_verify(x509cert, pubkey);
	BIO_printf(out, "X509_verify: %d, ", err);
    if (err < 0) {
        BIO_printf(out, "Signature verification problems....\n");
    } else if (err == 0) {
        BIO_printf(out, "Signature did not match the certificate\n");
    } else {
        BIO_printf(out, "Signature ok\n");
    }

	//X509_get0_uids (Issuer Unique ID / Subject Unique ID)

	// X509v3 extensions
	const ASN1_OCTET_STRING *skid = X509_get0_subject_key_id(x509cert);
	BIO_printf(out, "Subject key id: ");
	hexdump(out, skid->data, skid->length);
	BIO_printf(out, "\n");

	const ASN1_OCTET_STRING *akid = X509_get0_authority_key_id(x509cert);
	BIO_printf(out, "Authority key id: ");
	hexdump(out, akid->data, akid->length);
	BIO_printf(out, "\n");

	// const GENERAL_NAMES *X509_get0_authority_issuer(X509 *x);

	const ASN1_INTEGER *authority_serial = X509_get0_authority_serial(x509cert);
	if (authority_serial) {
		BIGNUM *bn_auth_serial = ASN1_INTEGER_to_BN(authority_serial, NULL);
		char *asciiHex = BN_bn2hex(bn_auth_serial);
		BIO_printf(out, "Authority serial: %s\n", asciiHex);
		OPENSSL_free(asciiHex);
	}	
	
	// X509_get0_signature, X509_signature_print

	BIO_free(out);
	X509_free(x509cert);

}
