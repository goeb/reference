#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
	FILE* f = fopen(argv[1], "w");

	int i = 0;
	const char *data = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=+()/!:;?-$*%.";
	int size = strlen(data);

	while (1) {
		char c = data[i%size];
		fprintf(f, "%c", c);
		fflush(f);
		i++;
		fprintf(stderr, "\r%d: %c", i, c);
	}
	

}
