#include <stdio.h>

int base64_decode(char *dst, const char *src)
{
	unsigned int triplet = 0; // decoded triplet (from 4 b64 characters)
	unsigned int b64code;
	int src_index = 0;

	while (*src) {
		b64code = (unsigned char)*src;
		src_index++;

		/* alphabet defined in RFC 4648 */
		if (b64code >= 'A' && b64code <= 'Z') b64code = b64code - 'A';           // 0..25
		else if (b64code >= 'a' && b64code <= 'z') b64code = b64code - 'a' + 26; // 26..51
		else if (b64code >= '0' && b64code <= '9') b64code = b64code - '0' + 52; // 52..61
		else if (b64code == '+') b64code = 62;                                   // 62
		else if (b64code == '/') b64code = 63;                                   // 63
		else if (b64code == '=') {
			switch ((src_index-1) % 4) {
			case 0:
				fprintf(stderr, "invalid character '=' aligned on 4\n");
				return -1;
			case 1:
				fprintf(stderr, "invalid character '=' aligned on 4 + 1\n");
				return -1;
			case 2:
				if (*(src+1) != '=') {
					fprintf(stderr, "invalid character '=' followed by other\n");
					return -1;
				}
				// Two b64 characters encode 1 character
				*dst++ = (char) (triplet >> 4);
				return 0;
			case 3:
				// 3 b64 codes encode 2 characters
				*dst++ = (char) (triplet >> 10);
				*dst++ = (char) (triplet >> 2);
				return 0;
			}
	   } else {
			fprintf(stderr, "invalid base64 character: '%c'\n", *src);
			return -1;
		}

		triplet = (triplet << 6) | b64code;
		if (0 == (src_index % 4)) {
			*dst++ = (char) (triplet >> 16);
			*dst++ = (char) (triplet >> 8);
		 	*dst++ = (char) triplet;
	   	triplet = 0;
		}
		src++;
	}
	return 0;
}

int main()
{
	const char *b64 = "aGVsbG8x"; // "hello1"
	char decoded_buffer[32] = {};
	base64_decode(decoded_buffer, b64);
	printf("%s => %s\n", b64, decoded_buffer);

	b64 = "aGVsbG8xMg=="; // "hello12"
	base64_decode(decoded_buffer, b64);
	printf("%s => %s\n", b64, decoded_buffer);

	b64 = "aGVsbG8xMjM="; // "hello123"
	base64_decode(decoded_buffer, b64);
	printf("%s => %s\n", b64, decoded_buffer);

}
