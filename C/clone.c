#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


main()
{
	pid_t p = fork();
	if (p) {
		// in parent
		printf("parent: pid=%d\n", p);
		while (1) {
			int status;
			pid_t pid = waitpid(p, &status, WNOHANG | WUNTRACED | WCONTINUED);

			printf(	"status[%d]: WIFEXITED=%d, WEXITSTATUS=%d, WIFSIGNALED=%d, WTERMSIG=%d"
					"WCOREDUMP=%d, WIFSTOPPED=%d, WSTOPSIG=%d, WIFCONTINUED=%d\n",
				pid,
				WIFEXITED(status),
				WEXITSTATUS(status),
				WIFSIGNALED(status),
				WTERMSIG(status),
				WCOREDUMP(status),
				WIFSTOPPED(status),
				WSTOPSIG(status),
				WIFCONTINUED(status)
				);
			sleep(5);	
		}
	} else {
		// in child
		sleep(1);
		int i = 0;
		printf("child exiting now\n");
		return 12;
		while (i<10) {
			printf("child: my pid=%d\n", getpid());
			sleep(1);
			i++;
		}
	}	
}

