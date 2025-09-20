/*
 * Compile with:
 * gcc -o g_variant g_variant.c $(pkg-config --cflags --libs gio-2.0)
 *
 * Execution:
 * ./g_variant
 * test_string: hello world
 * test_array_of_strings: The quick brown fox 
 * test_array_of_bytes_1: 00 12 34 56 
 * test_array_of_bytes_2: 00 11 22 33 
 */

#include <gio/gio.h>
#include <stdint.h>

void test_string()
{
	const gchar *str;
	GVariant *value;
	
	value = g_variant_new("&s", "hello world");
	g_variant_get(value, "&s", &str);
	g_print("test_string: %s\n", str);
	/* no need to free str */
}

void test_array_of_strings()
{
	GVariantBuilder *builder;
	GVariant *value;
	
	builder = g_variant_builder_new(G_VARIANT_TYPE("as"));
	g_variant_builder_add(builder, "s", "The");
	g_variant_builder_add(builder, "s", "quick");
	g_variant_builder_add(builder, "s", "brown");
	g_variant_builder_add(builder, "s", "fox");
	value = g_variant_new("as", builder);
	g_variant_builder_unref(builder);
	
	GVariantIter *iter;
	gchar *str;
		
	g_variant_get(value, "as", &iter);
	g_print("test_array_of_strings: ");
	while (g_variant_iter_loop(iter, "s", &str)) {
		g_print("%s ", str);
	}
	g_print("\n");
	g_variant_iter_free(iter);
	
	g_variant_unref(value);
}

void test_array_of_bytes_1()
{
	GVariantBuilder *builder;
	GVariant *value;
	
	builder = g_variant_builder_new(G_VARIANT_TYPE("ay"));
	g_variant_builder_add(builder, "y", 0x00);
	g_variant_builder_add(builder, "y", 0x12);
	g_variant_builder_add(builder, "y", 0x34);
	g_variant_builder_add(builder, "y", 0x56);
	value = g_variant_new("ay", builder);
	g_variant_builder_unref(builder);
	
	GVariantIter *iter;
	uint8_t byte;
		
	g_variant_get(value, "ay", &iter);
	g_print("test_array_of_bytes_1: ");
	while (g_variant_iter_loop(iter, "y", &byte)) {
		g_print("%02x ", byte);
	}
	g_print("\n");
	g_variant_iter_free(iter);
	
	g_variant_unref(value);
}

void test_array_of_bytes_2()
{
	GVariant *value = g_variant_new_fixed_array(G_VARIANT_TYPE_BYTE, "\x00\x11\x22\x33", 4, 1);
	
	GVariantIter *iter;
	uint8_t byte;
		
	g_variant_get(value, "ay", &iter);
	g_print("test_array_of_bytes_2: ");
	while (g_variant_iter_loop(iter, "y", &byte)) {
		g_print("%02x ", byte);
	}
	g_print("\n");
	g_variant_iter_free(iter);
	
	g_variant_unref(value);
}

int main()
{
	test_string();
	test_array_of_strings();
	test_array_of_bytes_1();
	test_array_of_bytes_2();
}
