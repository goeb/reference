
/*
 * gcc g_strv_builder.c $(pkg-config --cflags glib-2.0) $(pkg-config --libs glib-2.0)
 */

#include <glib.h>
#include <stdio.h>

void print_strv(gchar **words)
{
	gchar **word = words;
	while (*word) {
		printf("%s, ", *word);
		word++;
	}
	printf("\n");
}

int main()
{
	const char *sentence = "The quick brown fox jumps over the lazy dog";
	gchar **words = g_strsplit(sentence, " ", -1);

	print_strv(words);

	const char *sentence2 = "and more ...";
	gchar **words2 = g_strsplit(sentence2, " ", -1);

	GStrvBuilder *builder = g_strv_builder_new();
	g_strv_builder_addv(builder, (const char **)words);
	g_strv_builder_addv(builder, (const char **)words2);
	gchar **words1and2 = g_strv_builder_end(builder);
	g_strv_builder_unref(builder);

	print_strv(words1and2);

	g_strfreev(words);
	g_strfreev(words2);
	g_strfreev(words1and2);
}
