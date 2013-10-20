#include <stdio.h>

main()
{
    char first[1000];
    FILE *procMountsFile = fopen ( "toto", "r" );
    char *x = fgets(first, 1000, procMountsFile);
    printf("first=<%s>\n", first);
}
