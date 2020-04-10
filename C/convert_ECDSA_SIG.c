#include <stdio.h>
#include <openssl/ec.h>
#include <openssl/bn.h>

/* Compilation: link with openssl
 *     gcc -o convert_ECDSA_SIG convert_ECDSA_SIG.c  -lssl -lcrypto
 */

/* Example output (hexdumped):
 *    R has 3 leading zeros
 *    S starts with 0x88
 *
 * $ hd signature
 * 00000000  00 00 00 34 35 36 37 38  39 30 31 32 33 34 35 36  |...4567890123456|
 * 00000010  37 38 39 30 31 32 33 34  35 36 37 38 39 30 31 32  |7890123456789012|
 * 00000020  88 34 35 36 37 38 39 30  31 32 33 34 35 36 37 38  |.456789012345678|
 * 00000030  39 30 31 32 33 34 35 36  37 38 39 30 30 31 32 0a  |901234567890012.|
 *
 * $ convert_ECDSA_SIG < signature | openssl asn1parse -inform DER
 * R: 3435363738393031323334353637383930313233343536373839303132
 * S: 3435363738393031323334353637383930313233343536373839303132
 *     0:d=0  hl=2 l=  66 cons: SEQUENCE
 *     2:d=1  hl=2 l=  29 prim: INTEGER           :3435363738393031323334353637383930313233343536373839303132
 *    33:d=1  hl=2 l=  33 prim: INTEGER           :883435363738393031323334353637383930313233343536373839303031320A

 * $ convert_ECDSA_SIG < signature | hd
 * R: 3435363738393031323334353637383930313233343536373839303132
 * S: 3435363738393031323334353637383930313233343536373839303132
 * 00000000  30 42 02 1d 34 35 36 37  38 39 30 31 32 33 34 35  |0B..456789012345|
 * 00000010  36 37 38 39 30 31 32 33  34 35 36 37 38 39 30 31  |6789012345678901|
 * 00000020  32 02 21 00 88 34 35 36  37 38 39 30 31 32 33 34  |2.!..45678901234|
 * 00000030  35 36 37 38 39 30 31 32  33 34 35 36 37 38 39 30  |5678901234567890|
 * 00000040  30 31 32 0a                                       |012.|
 */

#define SIG_RS_SIZE 32

int usage(const char *progname)
{
    printf("Usage: %s\n", progname);
    printf("\n"
           "Convert a R,S signature (read from STDIN) to DER format (to STDOUT).\n"
           "\n");
    return 1;
}

void dump_bn(BIGNUM *bn, const char *label)
{
	char *bn_str = BN_bn2hex(bn);
    fprintf(stderr, "%s: %s\n", label, bn_str);
    OPENSSL_free(bn_str);
}

int convert_rs(unsigned char sig_r[SIG_RS_SIZE], unsigned char sig_s[SIG_RS_SIZE])
{
    int err, n;
    BIGNUM *bn_r, *bn_s;
    ECDSA_SIG *ecdsa_sig;

    // WARNING: missings deallocations (OPENSSL_free)

    ecdsa_sig = ECDSA_SIG_new();

    // Convert R
    bn_r = BN_bin2bn(sig_r, SIG_RS_SIZE, 0);
    if (!bn_r) {
        fprintf(stderr, "Cannot convert sig_r\n");
        return 1;
    }

	dump_bn(bn_r, "R");

    // Convert S
    bn_s = BN_bin2bn(sig_s, SIG_RS_SIZE, 0);
    if (!bn_s) {
        fprintf(stderr, "Cannot convert sig_s\n");
        return 1;
    }

	dump_bn(bn_s, "S");


	// Put together 
    err = ECDSA_SIG_set0(ecdsa_sig, bn_r, bn_s);
    if (!err) {
        fprintf(stderr, "ECDSA_SIG_set0 error\n");
		// TODO missing free ecdsa_sig, bn_r, bn_s
        return 1;
    }

    // Convert to DER
    unsigned char *pout = 0;
    n = i2d_ECDSA_SIG(ecdsa_sig, &pout);
    if (n < 0) {
        // error
        fprintf(stderr, "i2d_ECDSA_SIG error\n");
		// TODO missing free ecdsa_sig, bn_r, bn_s
        return 1;
    }

    n = fwrite(pout, n, 1, stdout);
    if (n != 1) {
        fprintf(stderr, "Cannot write result\n");
        return 1;
    }

    OPENSSL_free(pout);
	OPENSSL_free(bn_s);
	OPENSSL_free(bn_r);
    OPENSSL_free(ecdsa_sig);
    return 0;
}

int main(int argc, char **argv)
{
    unsigned char sig_r[SIG_RS_SIZE];
    unsigned char sig_s[SIG_RS_SIZE];
    size_t n;

    if (argc != 1) return usage(argv[0]);

    n = fread(sig_r, SIG_RS_SIZE, 1, stdin);
    if (n != 1) {
        fprintf(stderr, "Cannot read %d bytes (r)\n", SIG_RS_SIZE);
        return 1;
    }

    n = fread(sig_s, SIG_RS_SIZE, 1, stdin);
    if (n != 1) {
        fprintf(stderr, "Cannot read %d bytes\n", SIG_RS_SIZE);
        return 1;
    }

    return convert_rs(sig_r, sig_s);
}
