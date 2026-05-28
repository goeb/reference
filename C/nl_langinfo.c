// gcc gcc nl_langinfo.c
// ./a.out
// nl_langinfo(CODESET)=ANSI_X3.4-1968

#include <stdio.h>
#include <langinfo.h>

int main()
{
	printf("nl_langinfo(CODESET)=%s\n", nl_langinfo(CODESET));
}
