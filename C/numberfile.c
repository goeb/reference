#include <dirent.h>
#include <errno.h>
#include <libgen.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

void usage()
{
	printf("Usage: numberfile FILE  [-v]\n"
	       "\n"
	       "Rename FILE with a suffix .N, N being the maximum number (MAXN) plus one of all\n"
	       "the files in the same directory (DIR).  MAXN is determined by looking at the\n"
	       "files in DIR and extracting the first possible decimal number from them.\n"
	       "Numbers above 999'999'999 are considered invalid and ignored.\n"
	       "\n"
	       "Options\n"
	       "  -v  Verbose\n"
	       "\n"
	       "Example:\n"
	       "\n"
	       "    numberfile syslog.log\n"
	       "\n"
	       "If the files are syslog.log, syslog.log.1, syslog33.log.2, the above command \n"
	       "will rename syslog.log to syslog.log.34.\n"
	);
	exit(1);
}


/* Get the first decimal number found in name
 *
 * @param name
 *     Must be a null-terminated string
 * @return
 * 	   positive integer if found
 * 	   -1 if no number found
 * 	   -2 if invalid number (eg: overflow)
 */
static int getn(const char *name)
{
	int n = -1; // not found
	// Look for the first digit 0-9
	unsigned int index = 0;
	while (name[index] != 0) {
		if (name[index] >= '0' && name[index] <= '9') {
			// Got a first digit
			unsigned int start = index;

			// Now, go to the last digit in the sequence
			unsigned int end = index;
			while (name[end] >= '0' && name[end] <= '9') end++;

			int length = end-start;
			// Prevent overflow.
			// As 2^31 = 2147483648 has 10 digit, consider only numbers with 9 digits or less.
			if (length > 9) {
				// Consider this number is invalid
				return -2;
			}
			unsigned long int ln = strtoul(name+start, 0, 10);
			// Cast to not long (overflow verified above)
			n = (int) ln;
			break;
		}
		index++;
	}
	return n;
}

int main(int argc, char **argv)
{
	int verbose = 0;
	const char *file = 0;
	if (argc < 2) usage();
	int arg;
	for(arg=1; arg < argc; arg++) {
		if (0==strcmp("-v", argv[arg])) {
			if (verbose) usage(); // already encountered "-v"
			verbose = 1;
		} else if (file) usage(); // already encountered FILE argument
		else file = argv[arg];
	}

	char *filename_copy = strdup(file);
	char *dir = dirname(filename_copy);

	DIR *d = opendir(dir);
	if (!d) {
		fprintf(stderr, "cannot opendir '%s': %s\n", dir, strerror(errno));
		return 1;
	}

	free(filename_copy);

	struct dirent *f;
	unsigned int maxn = 1;
	while ( (f = readdir(d)) ) {
		if (0 == strcmp(".", f->d_name)) continue;
		if (0 == strcmp("..", f->d_name)) continue;
		int n = getn(f->d_name);
		if (verbose) printf("Extracting N from %30s: %d\n", f->d_name, n);
		if (n > 0 && n > maxn) maxn = n;
	}
	closedir(d);

	if (verbose) printf("maxn: %u\n", maxn);

	// prepare space for a suffix of 10 digits (maxn < 10^10, but maxn+1 may be 10^10)
	const int size = strlen(file)+strlen(".0123456789");
	char *new_file = malloc(size);
	snprintf(new_file, size, "%s.%d", file, maxn+1);

	if (verbose) printf("rename %s -> %s\n", file, new_file);
	int err = rename(file, new_file);
	if (err) {
		fprintf(stderr, "cannot rename '%s' -> '%s': %s\n", file, new_file, strerror(errno));
		err = 1;
	} else {
		// print the name of the new file, as it may be useful for the caller
		printf("%s\n", new_file);
	}
	free(new_file);
	return err;
}
