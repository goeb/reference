/* Example:
 * extract_last_integer 
 * $ ./extract_last_integer ""
 * No terminating digit found
 * $ ./extract_last_integer "123"
 * Terminating integer: 123
 * $ ./extract_last_integer "name-123"
 * Terminating integer: 123
 * $ ./extract_last_integer "name/1/2/3/4"
 * Terminating integer: 4
 * $ ./extract_last_integer "name"
 * No terminating digit found
 */

#include <stdio.h>
#include <stdlib.h>

void usage()
{
	printf("usage: extract_last_integer STRING\n");
	exit(1);
}

int main(int argc, char **argv)
{
	if (argc != 2) usage();

	char *ptr = argv[1];
	// step 1: got to the end (first null character found)
	while (*ptr) ptr++;
	// step 2: come back while the character is in [0-9]
	while (ptr > argv[1] && (*(ptr-1) >= '0' && *(ptr-1) <= '9' ) ) {
		ptr --;
	}
	if (*ptr < '0' || *ptr > '9' ) printf("No terminating digit found\n");
	else {
		unsigned long int value = strtoul(ptr, NULL, 10);
		printf("Terminating integer: %lu\n", value);
	}
}
