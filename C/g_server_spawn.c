/* Compile with:
 * gcc -o g_server_spawn g_server_spawn.c $(pkg-config --cflags --libs gio-2.0)
 *
 * Execution
 * ./g_server_spawn
 * stdout-123
 * stderr-456
 * g_child_watch_add: pid=6444 ok
 * g_main_loop_run returned
 *
 */

#include <gio/gio.h>

typedef struct {
	GMainLoop *mainloop;
} context_t;

void callback_watch_pid(GPid pid, gint wait_status, gpointer data)
{
	gboolean is_success = g_spawn_check_wait_status(wait_status, NULL);
	if (is_success) {
		g_print("g_child_watch_add: pid=%d ok\n", pid);
	} else {
		g_print("g_child_watch_add: pid=%d error\n", pid);
	}
	g_spawn_close_pid(pid);

	context_t *ctx = (context_t*)data;
	g_main_loop_quit(ctx->mainloop);
}

gboolean start_process(gpointer data)
{
	GError *error = NULL;
	GPid pid;
	gchar *command[] = {"sh", "-c", "echo stdout-123; echo stderr-456 >&2", NULL};
	gboolean is_ok = g_spawn_async(NULL, command, NULL,
	                               G_SPAWN_DO_NOT_REAP_CHILD | G_SPAWN_SEARCH_PATH,
	                               NULL, NULL, &pid, &error);
	if (!is_ok) {
		g_print("g_spawn_async error: %s\n", error->message);
		g_error_free(error);
		return FALSE;
	}
	g_child_watch_add(pid, callback_watch_pid, data);

	return FALSE; // do not trigger again
}

int main(int argc, char **argv)
{
	context_t ctx;
	ctx.mainloop = g_main_loop_new(NULL, FALSE);
	g_timeout_add(1000 /* ms */, start_process, (gpointer)&ctx);

	g_main_loop_run(ctx.mainloop);
    g_print("g_main_loop_run returned\n");
	g_main_loop_unref(ctx.mainloop);

	return 0;
}
