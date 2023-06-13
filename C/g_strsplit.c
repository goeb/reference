/*
 * Compile with:
 * gcc -o g_strsplit g_strsplit.c $(pkg-config --cflags --libs gio-2.0)
 *
 * Example:
 *
 * $ ./g_strsplit "a b:c :d" " :" 88
 * With g_strsplit()
 *   token=a b:c
 *   token=d
 * With g_strsplit_set()
 *   token=a
 *   token=b
 *   token=c
 *   token=
 *   token=d
 *
 */

#include <gio/gio.h>
#include <stdio.h>
#include <stdlib.h>

void usage()
{
	printf("usage:g_strsplit STRING DELIMITER MAX\n");
	exit(1);
}

int main(int argc, char **argv)
{
	if (argc != 4) usage();

	printf("With g_strsplit()\n");
	gchar** tokens = g_strsplit(argv[1], argv[2], atoi(argv[3]));
	gchar** token = tokens;
	while (*token) {
		printf("  token=%s\n", *token);
		token++;
	}
	g_strfreev(tokens);

	printf("With g_strsplit_set()\n");
	tokens = g_strsplit_set(argv[1], argv[2], atoi(argv[3]));
	token = tokens;
	while (*token) {
		printf("  token=%s\n", *token);
		token++;
	}
	g_strfreev(tokens);


	return 0;
}

