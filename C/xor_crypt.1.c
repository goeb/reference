#include <stdio.h>

void crypt(char *output, char *input, int length, char *key)
{
	char *ptr_key;
	if (strlen(key) == 0) {
		fprintf(stderr, "crypt : invalid null key\n");
		return;
	}
	ptr_key = key;
	while (length>0) {
		*output = *input ^ *ptr_key;
		input ++;
		output ++;
		ptr_key ++;
		if (*ptr_key == 0) ptr_key = key;
	length --;
	}
}
