/*
 * Compile with:
 * gcc gdbus-example-listener.c $(pkg-config --cflags --libs dbus-1) $(pkg-config --cflags --libs gio-2.0) $(pkg-config --cflags --libs gio-unix-2.0)
 *
 * Test with:
 * dbus-send --session --type=signal /path/to/object com.example.signal345 string:hello
 *
 * Result:
 * sender_name=org.freedesktop.DBus
 * object_path=/org/freedesktop/DBus
 * interface_name=org.freedesktop.DBus
 * signal_name=NameAcquired
 * 
 * sender_name=org.freedesktop.DBus
 * object_path=/org/freedesktop/DBus
 * interface_name=org.freedesktop.DBus
 * signal_name=NameOwnerChanged
 * 
 * sender_name=:1.124
 * object_path=/path/to/object
 * interface_name=com.example
 * signal_name=signal345
 * message=hello
 * 
 * sender_name=org.freedesktop.DBus
 * object_path=/org/freedesktop/DBus
 * interface_name=org.freedesktop.DBus
 * signal_name=NameOwnerChanged
 *
 */
#include <stdio.h>
#include <gio/gio.h>
#include <stdlib.h>

#ifdef G_OS_UNIX
#include <gio/gunixfdlist.h>
/* For STDOUT_FILENO */
#include <unistd.h>
#endif

static void on_message(GDBusConnection *connection,
                       const gchar     *sender_name,
                       const gchar     *object_path,
                       const gchar     *interface_name,
                       const gchar     *signal_name,
                       GVariant        *parameters,
                       gpointer         user_data)
{
	printf("sender_name=%s\n", sender_name);
	printf("object_path=%s\n", object_path);
	printf("interface_name=%s\n", interface_name);
	printf("signal_name=%s\n", signal_name);

	if (0 == strcmp("signal345", signal_name) ) {
		const gchar *message;
		g_variant_get(parameters, "(s)", &message);
		printf("message=%s\n", message);
	}

	printf("\n");
}

int main (int argc, char *argv[])
{
	GMainLoop *loop;
	GError *error = NULL;

	GDBusConnection *c = g_bus_get_sync (G_BUS_TYPE_SESSION, NULL, &error);
	if (!c) {
		printf("g_bus_get_sync error: %p\n", error->message);
		printf("g_bus_get_sync error: %s\n", error->message);
		return 1;
	}

	g_dbus_connection_signal_subscribe (c,
	                                    NULL,
	                                    NULL,
	                                    NULL,
	                                    NULL,
	                                    NULL,                   /* arg0 */
	                                    G_DBUS_SIGNAL_FLAGS_NONE,
	                                    on_message,
	                                    NULL,
	                                    NULL);

	loop = g_main_loop_new (NULL, FALSE);
	g_main_loop_run (loop);

	return 0;
}
