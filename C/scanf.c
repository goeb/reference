#include <stdio.h>

main ()
{
	int rc, i;
	char buf[BUFSIZ+1];
	char tmp[BUFSIZ+1];
	char tmp2[BUFSIZ+1];
    int x;
    int y;

	while (fgets (buf, BUFSIZ, stdin)) {
        //rc = sscanf (buf, "%[^=] = %d , %d", tmp, &x, &y);
		//printf ("rc=%d, tmp=%s, x=%d, y=%d\n", rc, tmp, x, y);
		//rc = sscanf (buf, "%s = %s", tmp, tmp2);
        //printf ("rc=%d, tmp=%s, tmp2=%s\n", rc, tmp, tmp2);
		rc = sscanf (buf, "%[^=] = %s", tmp, tmp2);
        printf ("rc=%d, tmp=%s, tmp2=%s\n", rc, tmp, tmp2);
	}
}
