/*
 * Original file: xfce4-settings-4.12.4/dialogs/accessibility-settings/find-cursor.c
 *
 * Compile with:
 * gcc -o highlight-cursor highlight-cursor-gtk3.c $(pkg-config --libs --cflags glib-2.0) $(pkg-config --libs --cflags gtk+-3.0)
 */

/*
 *  Copyright(c) 2018 Simon Steinbeiß <simon@xfce.org>
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Library General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License along
 *  with this program; if not, write to the Free Software Foundation, Inc.,
 *  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */

#ifdef HAVE_STDLIB_H
#include <stdlib.h>
#endif

#include <sys/stat.h>
#include <sys/types.h>

#include <glib.h>
#include <gtk/gtk.h>

#include <gdk/gdkx.h>
#include <math.h>

/* size of the window and circles */
#define CIRCLE_SIZE 500
guint64 CIRCLE_RADIUS = 25;

GdkPixbuf *pixbuf = NULL;
gint screenshot_offset_x, screenshot_offset_y;

/* gdk_cairo_set_source_pixbuf() crashes with 0,0 */
gint workaround_offset = 1;

static void usage() {
    printf("Usage: highlight-cursor [--size SIZE]\n");
    exit(1);
}

static gboolean timeout(gpointer data) {
    GtkWidget *widget = GTK_WIDGET(data);
    gtk_widget_queue_draw(widget);
    return TRUE;
}

static GdkPixbuf * get_rectangle_screenshot(gint x, gint y) {
    GdkPixbuf *screenshot = NULL;
    GdkWindow *root_window = gdk_get_default_root_window();
    gint width = CIRCLE_SIZE + workaround_offset;
    gint height = CIRCLE_SIZE + workaround_offset;

    /* cut down screenshot if it's out of bounds */
    if (x < 0) {
        width += x;
        x = 0;
    }
    if (y < 0) {
        height += y;
        y = 0;
    }

    screenshot = gdk_pixbuf_get_from_window(root_window,
                                             x, y,
                                             width, height);
    return screenshot;
}



static gboolean find_cursor_motion_notify_event(GtkWidget      *widget,
                                 GdkEventMotion *event,
                                 gpointer        userdata) {
    gtk_window_move(GTK_WINDOW(widget), event->x_root - CIRCLE_RADIUS, event->y_root - CIRCLE_RADIUS);
    return FALSE;
}



static gboolean find_cursor_window_composited(GtkWidget *widget) {
    gboolean     composited;
    GdkScreen   *screen = gtk_widget_get_screen(widget);
    GdkVisual   *visual = gdk_screen_get_rgba_visual(screen);

    if (gdk_screen_is_composited(screen))
       composited = TRUE;
    else
    {
        visual = gdk_screen_get_system_visual(screen);
        composited = FALSE;
    }

    gtk_widget_set_visual(widget, visual);
    return composited;
}



static void find_cursor_window_destroy(GtkWidget *widget,
                            gpointer   user_data) {
    if (pixbuf)
        g_object_unref(pixbuf);
    gtk_main_quit();
}



static gboolean
find_cursor_window_draw(GtkWidget      *widget,
                        cairo_t        *cr,
                        gpointer        user_data) {
    int i = 0;
    int arcs = 1;
    gboolean composited = GPOINTER_TO_INT(user_data);

    if (composited) {
        cairo_set_operator(cr, CAIRO_OPERATOR_SOURCE);
        cairo_set_source_rgba(cr, 1.0, 1.0, 1.0, 0.0);
    }
    else {
        if (pixbuf) {
            if (screenshot_offset_x > 0) screenshot_offset_x = 0;
            if (screenshot_offset_y > 0) screenshot_offset_y = 0;

            gdk_cairo_set_source_pixbuf(cr, pixbuf,
                                         0 - screenshot_offset_x - workaround_offset,
                                         0 - screenshot_offset_y - workaround_offset);
        }
        else
            g_warning("Something with the screenshot went wrong.");
    }

    cairo_paint(cr);

    cairo_set_line_width(cr, 3.0);
    cairo_translate(cr, CIRCLE_RADIUS, CIRCLE_RADIUS);

    /* draw fill */
    cairo_arc(cr, 0, 0, CIRCLE_RADIUS, 0, 2 * M_PI);
    cairo_set_source_rgba(cr, 1.0, 0.0, 0.0, 0.5);
    cairo_fill(cr);

    return FALSE;
}
static void handle_method_call(GDBusConnection       *connection,
                               const gchar           *sender,
                               const gchar           *object_path,
                               const gchar           *interface_name,
                               const gchar           *method_name,
                               GVariant              *parameters,
                               GDBusMethodInvocation *invocation,
                               gpointer               user_data)
{
    if (g_strcmp0(method_name, "Stop") == 0) {
        g_dbus_method_invocation_return_value(invocation, NULL);
        exit(0);
    } else {
        g_dbus_method_invocation_return_dbus_error(invocation, "org.highlight-cursor.Failed",
                                                               "Invalid method name");
    }

}
/* Introspection data for the service we are exporting */
static const gchar introspection_xml[] =
  "<node>"
  "  <interface name='org.highlightcursor'>"
  "    <method name='Stop'/>"
  "  </interface>"
  "</node>";

static const GDBusInterfaceVTable interface_vtable =
{
  handle_method_call,
  NULL,
  NULL,
  { 0 }
};
 
static void on_bus_acquired(GDBusConnection *connection, const gchar *name, gpointer user_data)
{
    printf("on_bus_acquired\n");
    guint registration_id;
    static GDBusNodeInfo *introspection_data = NULL;
    introspection_data = g_dbus_node_info_new_for_xml(introspection_xml, NULL);
    registration_id = g_dbus_connection_register_object(connection,
                                                        "/org/HighlightCursor",
                                                        introspection_data->interfaces[0],
                                                        &interface_vtable,
                                                        NULL,  /* user_data */
                                                        NULL,  /* user_data_free_func */
                                                        NULL); /* GError** */
}

static void on_name_acquired(GDBusConnection *connection, const gchar *name, gpointer user_data)
{
    printf("on_name_acquired\n");
}

static void on_name_lost(GDBusConnection *connection, const gchar *name, gpointer user_data)
{
    printf("on_name_lost\n");
  exit (1);
}


static void start_dbus() {
    printf("start_dbus\n");
    guint owner_id = g_bus_own_name (G_BUS_TYPE_SESSION,
                                     "org.highlightcursor",
                                     G_BUS_NAME_OWNER_FLAGS_NONE,
                                     on_bus_acquired,
                                     on_name_acquired,
                                     on_name_lost,
                                     NULL,
                                     NULL);

}

static int try_stop_running_instance()
{
    GError *error = NULL;
    GDBusConnection *connection = g_bus_get_sync(G_BUS_TYPE_SESSION, NULL, &error);
    if (error) return -1;

    GDBusProxy *proxy = g_dbus_proxy_new_sync(connection, G_DBUS_PROXY_FLAGS_NONE, NULL,
                       "org.highlightcursor",
                       "/org/HighlightCursor",
                       "org.highlightcursor",
                       NULL,
                       &error);
    if (error) return -2;

    g_dbus_proxy_call_sync(proxy,
                        "Stop", // Remote method name
                        NULL,
                        G_DBUS_CALL_FLAGS_NONE,
                        1000, // timeout (ms) 
                        NULL,
                        &error);
    if (error) return -3;

    g_dbus_connection_close_sync(connection, NULL, &error);
    if (error) return -4;

    return 0; // success
}

gint main(gint argc, gchar **argv) {
    GError        *error = NULL;
    GtkWidget     *window;
    GdkDisplay    *display;
    GdkSeat       *seat;
    GdkDevice     *device;
    GdkScreen     *screen;
    gint           x,y;
    gboolean       composited;

    gtk_init(&argc, &argv);

    argc--; argv++; // skip the program name
    while (argc) {
        if (0 == g_strcmp0(argv[0], "--size")) {
            if (argc < 2) usage();
            CIRCLE_RADIUS = g_ascii_strtoull(argv[1], NULL, 10);
            if (CIRCLE_RADIUS == 0) {
                printf("Invalid size\n");
                exit(1);
            }
            argc -= 2; argv += 2; // consume the 2 arguments
        } else usage();
    }

    int err = try_stop_running_instance();
    if (!err) {
        // previous instance stopped
        exit(0);
    }
    printf("try_stop_running_instance() -> %d\n", err);
    // else, run normally

    /* just get the position of the mouse cursor */
    display = gdk_display_get_default();
    seat = gdk_display_get_default_seat(display);
    device = gdk_seat_get_pointer(seat);
    screen = gdk_screen_get_default();
    gdk_device_get_position(device, &screen, &x, &y);

    /* popup tells the wm to ignore if parts of the window are offscreen */
    window = gtk_window_new(GTK_WINDOW_POPUP);
    gtk_container_set_border_width(GTK_CONTAINER(window), 0);
    gtk_window_set_resizable(GTK_WINDOW(window), FALSE);
    gtk_window_set_default_size(GTK_WINDOW(window), CIRCLE_SIZE, CIRCLE_SIZE);
    gtk_widget_set_size_request(GTK_WIDGET(window), CIRCLE_SIZE, CIRCLE_SIZE);
    gtk_window_set_decorated(GTK_WINDOW(window), FALSE);
    gtk_widget_set_app_paintable(GTK_WIDGET(window), TRUE);
    gtk_window_set_skip_taskbar_hint(GTK_WINDOW(window), FALSE);

    /* center the window around the mouse cursor */
    gtk_window_move(GTK_WINDOW(window), x - CIRCLE_RADIUS, y - CIRCLE_RADIUS);

    /* check if we're in a composited environment */
    composited = find_cursor_window_composited(GTK_WIDGET(window));

    /* with compositor: make the circles follow the mouse cursor */
    if (composited) {
        gtk_widget_set_events(GTK_WIDGET(window), GDK_POINTER_MOTION_MASK);
        g_signal_connect(G_OBJECT(window), "motion-notify-event",
                          G_CALLBACK(find_cursor_motion_notify_event), NULL);
    }
    /* fake transparency by creating a screenshot and using that as window bg */
    else {
        /* this offset has to match the screenshot */
        screenshot_offset_x = x - CIRCLE_RADIUS - workaround_offset;
        screenshot_offset_y = y - CIRCLE_RADIUS - workaround_offset;

        pixbuf = get_rectangle_screenshot(screenshot_offset_x, screenshot_offset_y);
        if (!pixbuf)
            g_warning("Getting screenshot failed");
    }

    g_signal_connect(G_OBJECT(window), "draw",
                      G_CALLBACK(find_cursor_window_draw), GINT_TO_POINTER (composited));
    g_signal_connect(G_OBJECT(window), "destroy",
                      G_CALLBACK(find_cursor_window_destroy), NULL);


    gtk_widget_show_all(GTK_WIDGET(window));

    timeout(window);

    start_dbus();

    gtk_main();

    return 0;
}
