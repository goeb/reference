#include <string.h>
/* try this program with the following args :

a.out "/12345/67//890/"
a.out "12345/67//890/"
a.out "12345/67/890"
a.out "123/ /45/67/890"

*/
main (int argc, char **argv)
{
	char *ptr;
	if (argc != 2) exit (0);

	printf ("1. argv[1]=%s\n", argv[1]);
	ptr = strtok (argv[1], "/");
	printf ("2. argv[1]=%s\n", argv[1]);
	while (ptr != NULL)
	{
		printf ("ptr=%s\n", ptr);
		ptr = strtok (NULL, "/");
	}
}
