#include <stdio.h>

unsigned long int f(unsigned long int x, int * counter)
{
    (*counter)++;
    if (x==1) return 1;
    return x*f(x-1, counter);
}

main(int argc, char **argv)
{
    int counter = 0;
    unsigned long int x = f(atoi(argv[1]), &counter);
    int i = 0;
    for (i=0; i< atoi(argv[2]); i++) x = f(atoi(argv[1]), &counter);
    printf("result=%lu, counter=%d\n", x, counter);
}
