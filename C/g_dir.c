/*
 * gcc -o g_dir g_dir.c $(pkg-config --cflags --libs gio-2.0)
 * 
 * usage: g_dir [DIRECTORY]
 */

#include <glib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
	const char *dirpath = ".";
	if (argc > 1) dirpath = argv[1];
	GDir* dir = g_dir_open(dirpath, 0, NULL);
	if (!dir) {
		fprintf(stderr, "Cannot open dir: %s\n", dirpath);
		return 1;
	}
	while (1) {
		const gchar *filename = g_dir_read_name(dir);
		if (!filename) break;
		printf("%s\n", filename);
	}
	
	g_dir_close(dir);
}
