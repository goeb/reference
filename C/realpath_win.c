#include <windows.h>
#include <stdio.h>

int main(int argc, char **argv)
{
	if (argc != 2) {
		fprintf(stderr, "usage: %s <file>\n", argv[0]);
		return 1;
	}

	char resolved_path[MAX_PATH];
	GetFullPathName(argv[1], MAX_PATH, resolved_path, NULL);

	printf("%s\n", resolved_path);
}
