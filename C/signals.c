#include <stdio.h>
#include <sys/types.h>
#include <signal.h>
#include <unistd.h>

#define LOG(...) { printf("%s/%d: ", name, getpid()); printf(__VA_ARGS__); printf("\n");}

char *name;
int handleCount = 0;
int sharedRessource = 333;
void handleSig(int x)
{
        static b = 1;
    LOG("handleSig(%d) starting...[%d]", x, handleCount);
    if (b) sleep(10);
    b = 0;

    handleCount++;
    LOG("handleSig(%d) ...ending", x);
}
void parent()
{
    sleep(10);
    while (1) {
        LOG("main loop beginning");
        sleep(1);
        LOG("main loop ending");
    }
    LOG("Exiting...");
}
void child()
{
    int count = 0;
    while(1) {
        LOG("kill(%d, SIGUSR1) [%d]", getppid(), count);
        int r = kill(getppid(), SIGRTMIN+1);
        //LOG("kill: r=%d", r);
        //usleep(100);
        count++;
        if (count>100000) break;
    }
    sharedRessource = 0;
    LOG("Exiting...");
}
int main(int argc, char **argv)
{
    struct sigaction action_fin, old;
    // positionnement des signaux SIGTERM
    action_fin.sa_handler = handleSig;
    sigemptyset(&action_fin.sa_mask);
    action_fin.sa_flags = 0;
    int r = sigaction(SIGRTMIN+1, &action_fin, NULL);
    LOG("sigaction: r=%d", r);
    pid_t x = fork();

    if (x>0) {
        // in the parent
        name = "parent";
        LOG("starting...");
        parent();
    } else {
        // in the child
        name = "child";
        LOG("starting...");
        child();
    }
}
