
#include <stdio.h>
#include <sys/types.h>

#include <signal.h>
#include <unistd.h>


#define LOG(...) { printf("%s: ", name); printf(__VA_ARGS__); printf("\n");}
char *name;

void handleSig(int x)
{
	LOG("handleSig(%d)", x);
}

void parent() 
{


	while (1)  {
		sleep(1);
	}
	LOG("Exiting...");
}

void child()
{
	while(1) {
		kill(getppid(), SIGUSR1);
		break;
	}

	LOG("Exiting...");
}

int main(int argc, char **argv)
{
	struct sigaction action_fin;

	// positionnement des signaux SIGTERM
	action_fin.sa_handler = handleSig;
	sigemptyset(&action_fin.sa_mask);
	action_fin.sa_flags = 0;
	sigaction(SIGUSR1, &action_fin, NULL);
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
