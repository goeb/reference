#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/wait.h>


#define PATH_MAX 1000

int testPopenRead()
{
	printf("testPopenRead...\n");
	FILE *fp;
	int status;
	char path[PATH_MAX];

	fp = popen("./test.sh", "r");
	if (fp == NULL) {
		printf("popen error: %s\n", strerror(errno));
		return 1;
	}

	while (fgets(path, PATH_MAX, fp) != NULL) {
		printf("xxx: %s", path);
	}


	status = pclose(fp);
	printf("status=%d, WEXITSTATUS(status)=%d\n", status, WEXITSTATUS(status));
	if (status == -1) {
		printf("pcloseerror: %s\n", strerror(errno));
	} else {
		/* Use macros described under wait() to inspect `status' in order
		   to determine success/failure of command executed by popen() */
	}
}
int testPopenWrite()
{
	printf("testPopenWrite...\n");
	FILE *fp;
	int status;
	char data[PATH_MAX];

	fp = popen("awk '{print \"yyy: \" $0;}' ", "w");
	if (fp == NULL) {
		printf("popen error: %s\n", strerror(errno));
		return 1;
	}

	// read from stdin and redirect to pipe
	while (fgets(data, PATH_MAX, stdin) != NULL) {
		fprintf(fp, "xxx: %s", data);
	}

	status = pclose(fp);
	if (status == -1) {
		printf("pcloseerror: %s\n", strerror(errno));
	} else {
		/* Use macros described under wait() to inspect `status' in order
		   to determine success/failure of command executed by popen() */
	}
}



int main(int argc, char **argv)
{

	if (argc <= 1) return testPopenRead();
	else return testPopenWrite();
}
