#include <stdio.h> 
#include <execinfo.h> 
#include <stdlib.h>

void fbacktrace(void)
{
    void *addresses[10];
    char **strings;

    int size = backtrace(addresses, 10);
    strings = backtrace_symbols(addresses, size);
    printf("Stack frames: %d\n", size);
    int i;
    for(i = 0; i < size; i++)
    {
        printf("%d: %X\n", i, (int)addresses[i]);
        printf("%s\n", strings[i]);
    }
    free(strings);
}
void f(char *s)
{
    fbacktrace();
}

main()
{
    f("toto");
}
