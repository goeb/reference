/*
 * Compile with:
 * gcc dbus-server-example.c $(pkg-config --cflags --libs dbus-1)
 */
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <dbus/dbus.h>

const char *version = "0.1";

/*
 * TestInterface
 *
 * For testing:
 * dbus-send --session --print-reply --dest=org.example.TestServer /org/example/TestObject org.example.TestInterface.Ping
 */
DBusHandlerResult message_handler(DBusConnection *conn, DBusMessage *message, void *data)
{
	DBusHandlerResult result;
	DBusMessage *reply = NULL;
	DBusError err;

	fprintf(stderr, "Message: %s.%s on %s\n",
		dbus_message_get_interface(message),
		dbus_message_get_member(message),
		dbus_message_get_path(message));

	dbus_error_init(&err);

	if (dbus_message_is_method_call(message, "org.example.TestInterface", "Ping")) {
		const char *pong = "Pong";

		if (!(reply = dbus_message_new_method_return(message)))
			goto fail;

		dbus_message_append_args(reply,
					 DBUS_TYPE_STRING, &pong,
					 DBUS_TYPE_INVALID);

	} else {
		return DBUS_HANDLER_RESULT_NOT_YET_HANDLED;
	}

fail:
	if (dbus_error_is_set(&err)) {
		if (reply)
			dbus_message_unref(reply);
		reply = dbus_message_new_error(message, err.name, err.message);
		dbus_error_free(&err);
	}

	/*
	 * In any cases we should have allocated a reply otherwise it
	 * means that we failed to allocate one.
	 */
	if (!reply)
		return DBUS_HANDLER_RESULT_NEED_MEMORY;

	/* Send the reply which might be an error one too. */
	result = DBUS_HANDLER_RESULT_HANDLED;
	if (!dbus_connection_send(conn, reply, NULL))
		result = DBUS_HANDLER_RESULT_NEED_MEMORY;
	dbus_message_unref(reply);

	return result;
}


const DBusObjectPathVTable server_vtable = {
	.message_function = message_handler
};


int main(void)
{
	DBusConnection *conn;
	DBusError err;
	int rv;

	dbus_error_init(&err);

	/* connect to the daemon bus */
	conn = dbus_bus_get(DBUS_BUS_SESSION, &err);
	if (!conn) {
		fprintf(stderr, "Failed to get a session DBus connection: %s\n", err.message);
		goto fail;
	}

	rv = dbus_bus_request_name(conn, "org.example.TestServer", DBUS_NAME_FLAG_REPLACE_EXISTING , &err);
	if (rv != DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER) {
		fprintf(stderr, "Failed to request name on bus: %s\n", err.message);
		goto fail;
	}

	if (!dbus_connection_register_object_path(conn, "/org/example/TestObject", &server_vtable, NULL)) {
		fprintf(stderr, "Failed to register a object path for 'TestObject'\n");
		goto fail;
	}

	printf("Starting dbus example server v%s\n", version);
	while(dbus_connection_read_write_dispatch(conn, 1000)) {
	}

	return EXIT_SUCCESS;
fail:
	dbus_error_free(&err);
	return EXIT_FAILURE;
}

