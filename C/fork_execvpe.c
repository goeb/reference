
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <stdio.h>


int main()
{
	pid_t p = fork();
	if (p) {
		// in parent
		printf("parent\n");
		sleep(1);
	} else {
		char *const argv[] = { "test-fh", 0 };
		char *const envp[] = { "x=y", 0 };
		int x = execvpe("ps", argv, envp);
		// this line is reached only in case the execve failed.
		printf("execve error: %s\n", strerror(errno));	
	}
}

