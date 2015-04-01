#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
	char s1[100];
	char s2[100];
	char s3[100];
	memset(s1, 0, sizeof(s1));
	memset(s2, 0, sizeof(s2));
	memset(s3, 0, sizeof(s3));

    int n = scanf("%d %9s %128s", s1, s2, s3);
	printf("n=%d, s1=%s, s2=%s, s3=%s\n", n, s1, s2, s3);
}
