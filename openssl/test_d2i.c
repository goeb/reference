
/*
 * gcc test_d2i.c  -l crypto
 */

#include <openssl/asn1.h>
#include <openssl/types.h>

#include <stdio.h>
#include <string.h>

unsigned char hexdigit2int(char c)
{
	if ((c >= '0') && (c <= '9')) return c - '0';
	if ((c >= 'a') && (c <= 'f')) return c - 'a' + 10;
	if ((c >= 'A') && (c <= 'F')) return c - 'A' + 10;
	fprintf(stderr, "cannot hexdigit2int(%c)\n", c);
	return 0;
}

int unhexlify(const char *hex, unsigned char *bin, size_t bin_len)
{
	size_t hex_len = strlen(hex);
	if (hex_len%2) {
		fprintf(stderr, "cannot unhexlify: odd length\n");
		return -1;
	}
	if (bin_len < hex_len/2) {
		fprintf(stderr, "cannot unhexlify: destination buffer too small\n");
		return -1;
	}
	unsigned char *bin_ptr = bin;
	for (int i=0; i<hex_len; i+=2) {
		unsigned char byte = hexdigit2int(hex[i])*16 + hexdigit2int(hex[i+1]);
		*bin_ptr = byte;
		bin_ptr++;
	}
	return bin_ptr-bin;
}

void test_sequence(const unsigned char *data, size_t length)
{
	const unsigned char *cur = data;
	int tag;
	long len;
	int xclass;

	int ret = ASN1_get_object(&cur, &len, &tag, &xclass, length);
	printf("ret=0x%x\n", ret);
	printf("V_ASN1_CONSTRUCTED: %s\n", (ret & V_ASN1_CONSTRUCTED)?"yes":"no");
	printf("V_ASN1_SEQUENCE: %s\n", (tag & V_ASN1_SEQUENCE)?"yes":"no");
	printf("delta ptr=%ld\n", cur - data);
	printf("len=%ld\n", len);
	printf("tag=0x%x\n", tag);
	printf("V_ASN1_APPLICATION: %s\n", (xclass==V_ASN1_APPLICATION)?"yes":"no");
}

void test_integer(const unsigned char *data, size_t length)
{
    ASN1_INTEGER *integer;
    integer = d2i_ASN1_INTEGER(NULL, &data, length);
	printf("integer=");
	if (integer->type == V_ASN1_NEG_INTEGER) printf("-");
	printf("0x");
	for (int i = 0; i < integer->length; i++) printf("%02X", integer->data[i]);
	printf("\n");
	ASN1_INTEGER_free(integer);
}

int main()
{
	unsigned char buffer[4096];
	int length = unhexlify("041445EBA2AFF492CFFFF12D518BA7A7219DF36DC80F", buffer, sizeof(buffer));
	printf("length=%d\n", length);
	const unsigned char *subjectKeyIdentifier_der = buffer;
	ASN1_OCTET_STRING *obj1 = NULL;
	const unsigned char *ptr = subjectKeyIdentifier_der;
	ASN1_OCTET_STRING *obj2 = d2i_ASN1_OCTET_STRING(&obj1, &ptr, length);

	printf("subjectKeyIdentifier_der=%p\n", subjectKeyIdentifier_der);
	printf("obj1=%p\n", obj1);
	printf("obj2=%p\n", obj2);
	printf("ptr=%p (delta=%ld)\n", ptr, ptr-subjectKeyIdentifier_der);

	length = unhexlify("3016801445EBA2AFF492CB82312D518BA7A7219DF36DC80F", buffer, sizeof(buffer));
	const unsigned char *authorityKeyIdentifier = buffer;
	test_sequence(authorityKeyIdentifier, length);

	length = unhexlify("3082010A0282010100AD0E15FFFF43805CB187F3B760F97112A5AEDC269488AAF4CEF520392858600CF880DAA9159532613CB5B128848A8ADC9F0A0C83177A8F90AC8AE779535C31842AF60F98323676CCDEDD3CA8A2EF6AFB21F25261DF9F20D71FE2B1D9FE1864D2125B5FF9581835BC47CDA136F96B7FD4B0383EC11BC38C33D9D82F18FE280FB3A783D6C36E44C061359616FE599C8B766DD7F1A24B0D2BFF0B72DA9E60D08E9035C678558720A1CFE56D0AC8497C3198336C22E987D0325AA2BA138211ED39179D993A72A1E6FAA4D9D5173175AE857D22AE3F014686F62879C8B1DAE45717C47E1C0EB0B492A656B3BDB297EDAAA7F0B7C5A83F9516D0FFAFFFEB085F18774F0203010001", buffer, sizeof(buffer));
	const unsigned char *subjectPublicKey = buffer;
	test_sequence(subjectPublicKey, length);

	length = unhexlify("0203012233", buffer, sizeof(buffer));
	test_integer(buffer, length);
	length = unhexlify("0201EC", buffer, sizeof(buffer));
	test_integer(buffer, length);
}
