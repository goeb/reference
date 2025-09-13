/*
 * gcc -o gdbus-example-client.c gdbus-example-client.c $(pkg-config --cflags --libs gio-2.0)
 *
 * Start gdbus-example-server
 *
 * gdbus-example-client org.gtk.GDBus.TestServer \
 *                      /org/gtk/GDBus/TestObject \
 *                      org.gtk.GDBus.TestInterface \
 *                      HelloWorld \
 *                      abcd
 * g_bus_get_sync(G_BUS_TYPE_SESSION,...) -> ok
 * g_dbus_proxy_new_sync -> ok
 * The server answered: 'You greeted me with 'abcd'. Thanks!'
* 
 *
 */
#include <gio/gio.h>
#include <stdio.h>
#include <stdlib.h>

int main(int arg, char **argv)
{
	GDBusProxy *proxy;
	GDBusConnection *conn;
	GError *error = NULL;

	conn = g_bus_get_sync(G_BUS_TYPE_SESSION, NULL, &error);
	g_assert_no_error(error);

	printf("g_bus_get_sync(G_BUS_TYPE_SESSION,...) -> ok\n");

	proxy = g_dbus_proxy_new_sync(conn,
	                  G_DBUS_PROXY_FLAGS_NONE, NULL, /* GDBusInterfaceInfo */
	                  argv[1], /* name */
	                  argv[2], /* object path */
	                  argv[3], /* interface */
	                  NULL,    /* cancellable */
	                  &error);
	g_assert_no_error(error);

	printf("g_dbus_proxy_new_sync -> ok\n");

	GVariant* parameters = g_variant_new("(s)", argv[5]);

	GVariant *result = g_dbus_proxy_call_sync(proxy,
	    argv[4], /* method name */
	    parameters, /* parameters */
	    G_DBUS_CALL_FLAGS_NONE,
	    -1, /* timeout */
	    NULL, /* cancellable */
	    &error);

	g_assert_no_error(error);

	const gchar *str;
	g_variant_get(result, "(&s)", &str);
	printf("The server answered: '%s'\n", str);
	g_variant_unref(result);
}
