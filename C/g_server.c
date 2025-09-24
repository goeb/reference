/* Compile with:
 * gcc -o g_server g_server.c $(pkg-config --cflags --libs gio-2.0)
 *
 * Execution:
 * ./g_server
 * hello 0
 * hello 1
 * hello 2
 * exiting in 1 s
 * g_main_loop_run returned
 */

#include <gio/gio.h>

typedef struct {
	GMainLoop *mainloop;
} context_t;

gboolean do_quit(gpointer data)
{
	context_t *ctx = (context_t*)data;
	g_main_loop_quit(ctx->mainloop);
	return FALSE;
}

gboolean function(gpointer data)
{
	static int counter = 0;
	g_print("hello %d\n", counter);
	counter++;
	if (counter >= 3) {
		g_print("exiting in 1 s\n");
		g_timeout_add(1000 /* ms */, do_quit, data);
		return FALSE;
	}
	return TRUE;
}

int main(int argc, char **argv)
{
	context_t ctx;
	ctx.mainloop = g_main_loop_new(NULL, FALSE);

	g_timeout_add(1000 /* ms */, function, (gpointer)&ctx);

	g_main_loop_run(ctx.mainloop);
	g_print("g_main_loop_run returned\n");

	g_main_loop_unref(ctx.mainloop);

	return 0;
}

