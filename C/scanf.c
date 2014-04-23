#include <stdio.h>
#include <string.h>

main()
{
	char s[100];
	memset(s, 41, 100);
    int n = scanf("%s", s);
	printf("s=%s, n=%d\n", s, n);
}
