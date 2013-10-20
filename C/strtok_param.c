#include <string.h>
/* try this program with the following arg (for example) :

a.out "a=123, b=tutu, c='+'"

*/
main (int argc, char **argv)
{
	char *param, *value;
	if (argc != 2) exit (0);

	param = strtok (argv[1], "=");
	while (param != NULL)
	{
		value = strtok (NULL, ",");
		printf ("[%s] -> [%s]\n", param, value);
		param = strtok (NULL, "=");
	}
}
