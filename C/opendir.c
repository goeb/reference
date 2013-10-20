
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <dirent.h>
#include <errno.h>
#include <string.h>
#include <dirent.h>

main() {
	int rc;
	DIR *d;
	struct dirent * f;
	char root[]="/home/fred/tmp";
	char path[100];
	struct stat S;
	d = opendir(root);
	if (!d) {
		printf("error: %s\n", strerror(errno));
		exit(1);
	}
	while (f = readdir(d)) {
		printf("+ %s", f->d_name);
		strcpy(path, root);
		strcat(path, "/");
		strcat(path, f->d_name);
		rc = stat(path, &S);
		printf(" - rc=%d", rc);
		printf(" - mtime=%d", S.st_mtime);
		if (S_ISDIR(S.st_mode)) printf(" -> DIR !\n");
		else printf("\n");
	}
	closedir(d);
}
