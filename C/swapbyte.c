/* works with standard input and output
 * INPUT : abcdef
 * OUTPUT : badcfe
 */
#include <stdio.h>

main()
{
	unsigned short s;
	char *p;
	char c;
	while (2==fread(&s, 1, 2, stdin)) {
		p=&s;
		c=p[1];
		p[1]=p[0];
		p[0]=c;
		fwrite(&s, 1, 2, stdout);
	}
}

