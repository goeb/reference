/*######### not working !!!!!!!!!!!!!*/
#include <stdio.h>
#define _XOPEN_SOURCE
#include <unistd.h>

main(int argc, char **argv)
{
	char buffer[64+1];
	char key[64]={	0,1,1,1,1,1,1,1,1,1, /* 1-10 */
			0,0,0,0,0,1,1,1,1,1, /* 11-20 */
			1,1,1,0,0,1,1,1,1,1, /* 21-30 */
			1,1,1,0,0,1,1,1,1,1, /* 31-40 */
			1,1,1,0,0,1,1,1,1,1, /* 41-50 */
			1,1,1,0,0,1,1,1,1,1, /* 51-60 */
			1,1,1,0 /* 61-64 */
			};

	if (argc != 2) return;
	setkey(key);
	strncpy(buffer, argv[1], 64);
	printf("%s\n", buffer);
	encrypt(buffer, 0);
	printf("%s\n", buffer);
	setkey(key);
	encrypt(buffer, 1);
	printf("%s\n", buffer);
}
/*
gcc -g -o crypt crypt.c -lcrypt
*/
