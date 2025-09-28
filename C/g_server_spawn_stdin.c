/* Compile with:
 * gcc -o g_server_spawn_stdin g_server_spawn_stdin.c $(pkg-config --cflags --libs gio-2.0)
 *
 * Execution:
 * ./g_server_spawn_stdin
 *
 * It shows how a daemon sends bytes to the stdin of a child process:
 * - nominal case (child consuming the bytes)
 * - child exits
 * - pipe full and blocks, then resumes
 * 
 */

#include <glib-unix.h>
#include <stdio.h>
#include <unistd.h>

void callback_watch_pid(GPid pid, gint wait_status, gpointer data)
{
	gboolean is_success = g_spawn_check_wait_status(wait_status, NULL);
	if (is_success) {
		g_print("callback_watch_pid: pid=%d ok\n", pid);
	} else {
		g_print("callback_watch_pid: pid=%d error\n", pid);
	}
	g_spawn_close_pid(pid);
}

gboolean feed_stdin_exit(gint fd, GIOCondition condition, gpointer user_data)
{
	static int counter = 100;
	counter--;
	g_print("feed_stdin_exit: condition=0x%x\n", condition);
	if (condition & G_IO_OUT) {
		char buffer[100];
		sprintf(buffer, "echo hello counter=%d\n", counter);
		ssize_t n = write(fd, buffer, strlen(buffer));
		g_print("feed_stdin_exit: write[%d]: n=%ld\n", counter, n);
		if (n < 0 && errno == EPIPE) {
			g_print("feed_stdin_exit: got EPIPE, termination of child\n");
			counter = -1;
		} else if (n < 0) {
			g_print("feed_stdin_exit: errno=%d\n", errno);
			counter = -1;
		}
	}
	if (counter <= 0) {
		close(fd);
		return G_SOURCE_REMOVE;
	}
	return G_SOURCE_CONTINUE;
}

gboolean feed_stdin_normal(gint fd, GIOCondition condition, gpointer user_data)
{
	static int counter = 10;
	counter--;
	g_print("feed_stdin_normal: condition=0x%x\n", condition);
	if (condition & G_IO_OUT) {
		char buffer[100];
		sprintf(buffer, "echo hello counter=%d\n", counter);
		ssize_t n = write(fd, buffer, strlen(buffer));
		g_print("feed_stdin_normal: write[%d]: n=%ld\n", counter, n);
		if (n < 0 && errno == EPIPE) {
			g_print("feed_stdin_normal: got EPIPE, termination of child\n");
			counter = -1;
		} else if (n < 0) {
			g_print("feed_stdin_exit: errno=%d\n", errno);
			counter = -1;
		}
	}
	if (counter <= 0) {
		close(fd);
		return G_SOURCE_REMOVE;
	}
	return G_SOURCE_CONTINUE;
}

gboolean feed_stdin_pipe_full(gint fd, GIOCondition condition, gpointer user_data)
{
	static int counter = 2500;
	counter--;
	g_print("%s: condition=0x%x\n", __func__, condition);
	if (condition & G_IO_OUT) {
		char buffer[100];
		sprintf(buffer, "line-0123456789-abcdefghijklmnopqrstuvwxyz\n");
		ssize_t n = write(fd, buffer, strlen(buffer));
		g_print("%s: write[%d]: n=%ld\n", __func__, counter, n);
		if (n < 0 && errno == EPIPE) {
			g_print("%s: got EPIPE, termination of child\n", __func__);
			counter = -1;
		} else if (n < 0) {
			g_print("%s: errno=%d\n", __func__, errno);
			counter = -1;
		}
	}
	if (condition & G_IO_ERR) {
		// happens when previous writings were blocked, then the child process exited.
		g_print("%s: G_IO_ERR\n", __func__);
		goto close_fd;
	}
	if (!(condition & G_IO_OUT) && !(condition & G_IO_ERR)) {
		g_print("%s: unexpected condition 0x%x\n", __func__, condition);
		goto close_fd;
	}
	if (counter <= 0) goto close_fd;

	return G_SOURCE_CONTINUE;
close_fd:
	close(fd);
	return G_SOURCE_REMOVE;
}

gboolean start_process_nominal(gpointer data)
{
	GError *error = NULL;
	gint fd_stdin;
	GPid pid;
	gchar *command[] = {"sh", "-c", "sh | sed -e 's/^/>>> /'", NULL};
	gboolean is_ok = g_spawn_async_with_pipes(NULL, command, NULL,
	                               G_SPAWN_DO_NOT_REAP_CHILD | G_SPAWN_SEARCH_PATH,
	                               NULL, NULL, &pid,
	                               &fd_stdin, NULL, NULL,
	                               &error);
	if (!is_ok) {
		g_print("g_spawn_async_with_pipes error: %s\n", error->message);
		g_error_free(error);
		return G_SOURCE_REMOVE;
	}
	g_unix_fd_add(fd_stdin, G_IO_OUT|G_IO_PRI|G_IO_ERR|G_IO_HUP, feed_stdin_normal, data);
	g_child_watch_add(pid, callback_watch_pid, NULL);

	return G_SOURCE_REMOVE; // do not trigger again
}


gboolean start_process_pipe_full(gpointer data)
{
	GError *error = NULL;
	gint fd_stdin;
	GPid pid;
	gchar *command[] = {"sh", "-c", "sleep 5; cat; sleep 1", NULL};
	gboolean is_ok = g_spawn_async_with_pipes(NULL, command, NULL,
	                               G_SPAWN_DO_NOT_REAP_CHILD | G_SPAWN_SEARCH_PATH,
	                               NULL, NULL, &pid,
	                               &fd_stdin, NULL, NULL,
	                               &error);
	if (!is_ok) {
		g_print("g_spawn_async_with_pipes error: %s\n", error->message);
		g_error_free(error);
		return G_SOURCE_REMOVE;
	}
	g_unix_fd_add(fd_stdin, G_IO_OUT|G_IO_PRI|G_IO_ERR|G_IO_HUP, feed_stdin_pipe_full, data);
	g_child_watch_add(pid, callback_watch_pid, NULL);

	return G_SOURCE_REMOVE; // do not trigger again
}

gboolean start_process_exit(gpointer data)
{
	GError *error = NULL;
	gint fd_stdin;
	GPid pid;
	gchar *command[] = {"sh", "-c", "exit 1", NULL};
	gboolean is_ok = g_spawn_async_with_pipes(NULL, command, NULL,
	                               G_SPAWN_DO_NOT_REAP_CHILD | G_SPAWN_SEARCH_PATH,
	                               NULL, NULL, &pid,
	                               &fd_stdin, NULL, NULL,
	                               &error);
	if (!is_ok) {
		g_print("g_spawn_async_with_pipes error: %s\n", error->message);
		g_error_free(error);
		return G_SOURCE_REMOVE;
	}
	g_unix_fd_add(fd_stdin, G_IO_OUT|G_IO_PRI|G_IO_ERR|G_IO_HUP, feed_stdin_exit, data);
	g_child_watch_add(pid, callback_watch_pid, NULL);

	return G_SOURCE_REMOVE; // do not trigger again
}

int main(int argc, char **argv)
{
	GMainLoop *mainloop;
	// ignore SIGPIPE, so that EPIPE errors on writing to stdin of child processes does not kill us
	signal(SIGPIPE, SIG_IGN);
	mainloop = g_main_loop_new(NULL, FALSE);
	g_idle_add(start_process_nominal, NULL);
	g_idle_add(start_process_exit, NULL);
	g_idle_add(start_process_pipe_full, NULL);
	g_main_loop_run(mainloop);
	g_print("g_main_loop_run returned\n");
	g_main_loop_unref(mainloop);

	return 0;
}
