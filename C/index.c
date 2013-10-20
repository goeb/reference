#include <string.h>
#include <strings.h>

main ()
{
	char *s = "12345'67890";
	char *ptr;

	ptr = index (s, '\'');
	printf ("ptr=%s\n", ptr);
}
