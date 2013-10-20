#include <stdio.h>
#undef BUFSIZ
#define BUFSIZ 10

main()
{
	char buffer[BUFSIZ+1];
	char cbuffer[BUFSIZ+1];
	int l;
	while (0<(l=fread(buffer, 1, BUFSIZ, stdin))) {
		crypt(cbuffer, buffer, l, "toto");
		fwrite(cbuffer, 1, l, stdout);
	}

}
/*
gcc crypt_stream.c -L. -lxor_crypt
*/
