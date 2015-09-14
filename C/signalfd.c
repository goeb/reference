#include <stdlib.h>
#include <sys/signalfd.h>
#include <stdio.h>
#include <poll.h>
#include <unistd.h>
#include <sys/types.h>
#include <signal.h>

void parent(int sigfd)
{
    fprintf(stderr, "%d: parent...\n", getpid());
    struct pollfd ufds[1];
    ufds[0].fd = sigfd;
    ufds[0].events = POLLIN;
    while (1) {
        int rv = poll(ufds, 1, 5000); // 5 second timeout
        if (rv == -1) {
            perror("poll");
        } else if (rv == 0) {
            fprintf(stderr, "Timeout occurred!\n");
        } else {
            if (ufds[0].revents & POLLIN) {
                fprintf(stderr, "got SIGCHLD\n");
                struct signalfd_siginfo si;
                int n = read(sigfd, &si, sizeof(si));
                fprintf(stderr, "sig-read: n=%d, sender=%d, exit-status=%d\n",
                        n, si.ssi_pid, si.ssi_status);
            }
        }
    }
}
void child(int duration)
{
    fprintf(stderr, "%d: child...\n", getpid());
    sleep(duration);
    exit(4);
}

int main()
{
    sigset_t sigset;
    sigemptyset(&sigset);
    sigaddset(&sigset, SIGCHLD);

    // Block the signals thet we handle using signalfd(), so they don't
    // cause signal handlers or default signal actions to execute.
    sigprocmask(SIG_BLOCK, &sigset, NULL);

    int sigfd = signalfd(-1, &sigset, SFD_CLOEXEC);

    pid_t p = fork();
    if (-1 == p) {
        perror("fork");
        exit(1);
    } else if (p) parent(sigfd);
    else child(2);

    fprintf(stderr, "%d: exiting...\n", getpid()); 
}
