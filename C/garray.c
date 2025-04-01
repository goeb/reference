
/*
 * gcc garray.c $(pkg-config --cflags glib-2.0) $(pkg-config --libs glib-2.0)
 */

#include <glib.h>
#include <stdio.h>

int main()
{
	gchar *data[3] = {"one", "two", NULL};
	gchar **ptr = data;

	GArray* array = g_array_new(TRUE, TRUE, sizeof(gchar*));
	gchar* ptr1 = "hello";
	gchar* ptr2 = "it's a nice day today";
	gchar* ptr3 = "END";
	g_array_append_val(array, ptr1);
	g_array_append_val(array, ptr2);
	g_array_append_val(array, ptr3);

	guint size = array->len;
	for (int i=0; i < size; i++) {
		gchar *value = g_array_index(array, gchar*, i);
		printf("value=%s\n", value);
	}

	g_array_free(array, TRUE);
}
