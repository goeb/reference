#include <stdio.h>
#include <stdlib.h>

#include "example1.h"
#include "config.h"

int main(int argc, char **argv)
{
	if (argc > 1) {
		fprintf(stderr, "%s error: argument not supported '%s'\n", PROGNAME, argv[1]);
		return EXIT_FAILURE;
	}
	printf("hello world: CONF_PATH=%s\n", CONF_PATH);
	return EXIT_SUCCESS;
}
