#include <stdio.h>

void usage(char *progname)
{
	fprintf(stderr, "Usage : %s string\n", progname);
	exit(1);
}

void crypt(char *output, char *input, int length, char *key, char *key2)
{
	char *ptr_key, *ptr_key2;
	if (strlen(key) == 0) {
		fprintf(stderr, "crypt : invalid null key\n");
		return;
	}
	ptr_key = key;
	ptr_key2 = key2;
	while (length>0) {
		*output = *input ^ *ptr_key ^ *ptr_key2;
		input ++;
		output ++;
		ptr_key ++;
		ptr_key2 ++;
		if (*ptr_key == 0) ptr_key = key;
		if (*ptr_key2 == 0) ptr_key2 = key2;
	length --;
	}
}

main (int argc, char **argv)
{
	char buffer[BUFSIZ+1];
	char result[BUFSIZ+1];
	char *key = "toto";
	if (argc != 2) usage(argv[0]);
	crypt(buffer, argv[1], strlen(argv[1]), key, "AZERTY");
	printf("%s\n", buffer);
	strncpy(result, buffer, BUFSIZ);
	crypt(buffer, result, strlen(result), key, "AZERTY");
	printf("%s\n", buffer);
}
