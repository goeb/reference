
/*
 * gcc g_strv_contains.c $(pkg-config --cflags glib-2.0) $(pkg-config --libs glib-2.0)
 */

#include <glib.h>
#include <stdio.h>

void test_contains(gchar **words, gchar *word)
{
	printf("Contains '%s'? ... ", word);
	if (g_strv_contains((const gchar * const *)words, word)) printf("yes");
	else printf("no");
	printf("\n");
}

int main()
{
	const char *sentence = "The quick brown fox jumps over the lazy dog";
	gchar **words = g_strsplit(sentence, " ", -1);
	gchar **word = words;
	while (*word) {
		printf("word=%s\n", *word);
		word++;
	}

	test_contains(words, "fo");
	test_contains(words, "fox");
	test_contains(words, "fox2");
	test_contains(words, "hello");

	g_strfreev(words);
}
