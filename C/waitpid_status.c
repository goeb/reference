       #include <sys/types.h>
       #include <sys/wait.h>
#include <stdio.h>
main() 
{
	int status = 256;
if (WIFEXITED(status)) printf("WIFEXITED");
else if (WEXITSTATUS(status)) printf("WEXITSTATUS");
else if (WIFSIGNALED(status)) printf("WIFSIGNALED");
else if (WTERMSIG(status)) printf("WTERMSIG");
else if (WCOREDUMP(status)) printf("WCOREDUMP");
else if (WIFSTOPPED(status)) printf("WIFSTOPPED");
else if (WSTOPSIG(status)) printf("WSTOPSIG");
else if (WIFCONTINUED(status)) printf("WIFCONTINUED");
printf("\n");
}
