/* Compile with:
 * gcc -o g_server_spawn_pipes g_server_spawn_pipes.c $(pkg-config --cflags --libs gio-2.0)
 *
 * Execution
 * ./g_server_spawn_pipes
 *
 */

#include <gio/gio.h>
#include <glib-unix.h>

typedef struct {
	GMainLoop *mainloop;
} context_t;

typedef struct {
	GMainLoop *mainloop;
	GPid pid;
	int connection_id;
	int fd_stdout;
	int fd_stderr;
} child_context_t;

void callback_watch_pid(GPid pid, gint wait_status, gpointer data)
{
	static int quit_after = 2;
	child_context_t *child_ctx = (child_context_t*)data;

	gboolean is_success = g_spawn_check_wait_status(wait_status, NULL);
	if (is_success) {
		g_print("callback_watch_pid: pid=%d ok\n", pid);
	} else {
		g_print("callback_watch_pid: pid=%d error\n", pid);
	}
	g_spawn_close_pid(pid);

	quit_after--;
	if (quit_after == 0) g_main_loop_quit(child_ctx->mainloop);
}

gboolean print_child_output(const char *label, gint fd, GIOCondition condition, gpointer user_data)
{
	child_context_t *child_ctx = (child_context_t*)user_data;
	int cnx_id = child_ctx->connection_id;

	if (condition & G_IO_IN) {
		guint8 buffer[10];
		ssize_t n;
		n = read(fd, buffer, sizeof(buffer)-1);
		if (n > 0) {
			buffer[n] = 0;
			g_print("%d: (%s) %s\n", child_ctx->connection_id, label, buffer); // assume printable characters only
		}
	}
	if (condition & G_IO_HUP) {
		g_print("%d: (%s end)\n", cnx_id, label);
		goto close_fd;
	}
	if (!(condition & G_IO_HUP) && !(condition == G_IO_IN)) {
		g_error("%d: (%s unexpected condition %d)\n", cnx_id, label, condition);
		goto close_fd;
	}

	return TRUE; // continue listening on this fd
close_fd:
	close(fd);
	return FALSE; // stop monitoring this fd
}

gboolean print_stdout(gint fd, GIOCondition condition, gpointer user_data)
{
	return print_child_output("stdout", fd, condition, user_data);
}

gboolean print_stderr(gint fd, GIOCondition condition, gpointer user_data)
{
	return print_child_output("stderr", fd, condition, user_data);
}

gboolean start_process(gpointer data)
{
	static int next_connection_id = 0;
	context_t *ctx = (context_t*)data;

	GError *error = NULL;
	gint standard_output;
	gint standard_error;
	GPid pid;
	gchar *command[] = {"sh", "-c", "echo $$:stdout-123456789012345; echo sleeping 3... >&2; sleep 3; echo $$:stdout-999", NULL};
	gboolean is_ok = g_spawn_async_with_pipes(NULL, command, NULL,
	                               G_SPAWN_DO_NOT_REAP_CHILD | G_SPAWN_SEARCH_PATH,
	                               NULL, NULL, &pid,
	                               NULL, &standard_output, &standard_error,
	                               &error);
	if (!is_ok) {
		g_print("g_spawn_async error: %s\n", error->message);
		g_error_free(error);
		return G_SOURCE_REMOVE;
	}
	child_context_t *child_ctx = g_new(child_context_t, 1);
	child_ctx->mainloop = ctx->mainloop;
	child_ctx->pid = pid;
	child_ctx->connection_id = next_connection_id;
	next_connection_id++;
	g_unix_fd_add(standard_output, G_IO_IN|G_IO_PRI|G_IO_ERR|G_IO_HUP, print_stdout, (gpointer)child_ctx);
	g_unix_fd_add(standard_error, G_IO_IN|G_IO_PRI|G_IO_ERR|G_IO_HUP, print_stderr, (gpointer)child_ctx);
	g_child_watch_add(pid, callback_watch_pid, (gpointer)child_ctx);

	return G_SOURCE_REMOVE; // do not trigger again
}

int main(int argc, char **argv)
{
	context_t ctx;
	ctx.mainloop = g_main_loop_new(NULL, FALSE);
	g_idle_add(start_process, (gpointer)&ctx);
	g_idle_add(start_process, (gpointer)&ctx);
	g_main_loop_run(ctx.mainloop);
	g_print("g_main_loop_run returned\n");
	g_main_loop_unref(ctx.mainloop);

	return 0;
}
