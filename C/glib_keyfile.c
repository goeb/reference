/*
 * Compile with:
 * $ gcc -o glib_keyfile glib_keyfile.c $(pkg-config --cflags --libs gio-2.0)
 *
 * Examples:
 *
 * $ printf "[init]\nx=111\n# This is a comment\n[colors]\nname=grey\ncode=#fff" | ./glib_keyfile
 * Groups: 2
 *   init
 *     x=111
 *   colors
 *     name=grey
 *     code=#fff
 * 
 * $ printf "[init]\nx=111\n[colors]\ny" | ./glib_keyfile
 * g_key_file_load_from_file error: Key file contains line “y” which is not a key-value pair, group, or comment
 *
 */

#include <gio/gio.h>
#include <stdio.h>
#include <stdlib.h>

void usage()
{
	printf("usage: glib_keyfile < KEYFILE\n");
	exit(1);
}

int read_from_stdin(gchar* buf, gsize buf_size)
{
	GIOChannel *in = g_io_channel_unix_new(0);
	GError *error = NULL;
	gsize bytes_read;
	GIOStatus status = g_io_channel_read_chars(in, buf, buf_size, &bytes_read, &error);
	switch(status) {
		case G_IO_STATUS_ERROR:
			printf("g_io_channel_read_chars error: %s\n", error->message);
			return -1;
			break;
		case G_IO_STATUS_NORMAL:
			break;
		case G_IO_STATUS_EOF:
			printf("g_io_channel_read_chars: eof\n");
			break;
		case G_IO_STATUS_AGAIN:
			printf("g_io_channel_read_chars: AGAIN\n");
			break;
		default:
			printf("g_io_channel_read_chars: OTHER\n");
			break;
	}
	//printf("bytes_read=%d\n", bytes_read);
	return bytes_read; // success
}

int main(int argc, char **argv)
{
	gchar data[4096+1];
	int data_size = read_from_stdin(data, 4096);
	if (data_size < 0) return 1;
	data[data_size] = 0;
	//printf("data=\n%s\n--\n", data);

	GKeyFile *key_file = g_key_file_new();
	GKeyFileFlags flags = G_KEY_FILE_NONE;
	GError *error = NULL;
	gboolean result = g_key_file_load_from_data(key_file,
	                                            data,
	                                            data_size,
												flags,
												&error);

	if (result == FALSE) {
		printf("g_key_file_load_from_file error: %s\n", error->message);
		g_error_free(error);
		return 1;
	}

	gsize n_groups;
	gchar **groups = g_key_file_get_groups(key_file, &n_groups);
	printf("Groups: %d\n", n_groups);
	int i;
	for (i=0; i<n_groups; i++) {
		const gchar *group = groups[i];
		printf("  %s\n", group);
		gsize n_keys;
		GError *error = NULL;
		gchar **keys = g_key_file_get_keys(key_file, group, &n_keys, &error);
		if (!keys) {
			printf("g_key_file_get_keys(%s) error: %s\n", group, error->message);
		} else {

			int j;
			for (j=0; j<n_keys; j++) {
				const gchar *key = keys[j];
				GError *error = NULL;
				gchar *value = g_key_file_get_string(key_file, group, key, &error);
				if (!value) {
					printf("g_key_file_get_string(%s, %s) error: %s\n", group, key, error->message);
				} else {
					printf("    %s=%s\n", key, value);
					g_free(value);
				}
			}
			g_strfreev(keys);
		}
	}
	g_strfreev(groups);
	return 0;
}

