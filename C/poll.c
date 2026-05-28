#include <stdlib.h>
#include <stdio.h>
#include <poll.h>
#include <unistd.h>
#include <sys/types.h>

void test_poll()
{
    fprintf(stderr, "%d: parent...\n", getpid());
    struct pollfd ufds[1];
    ufds[0].fd = 0; // stdin
    ufds[0].events = POLLIN;
    while (1) {
        int rv = poll(ufds, 1, 5000); // 5 second timeout
        if (rv == -1) {
            perror("poll");
        } else if (rv == 0) {
            fprintf(stderr, "Timeout occurred!\n");
        } else {
            if (ufds[0].revents & POLLIN) {
                fprintf(stderr, "POLLIN\n");
				char buffer[1024];
                int n = read(0, buffer, sizeof buffer);
                fprintf(stderr, "read: n=%d\n", n);
            }
        }
    }
}

int main()
{
    test_poll();
}
