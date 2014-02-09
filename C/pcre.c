
/** gcc pcre.c -lpcre */
#include <string.h>
#include <stdio.h>
#include "pcre.h"

int main (int argc, char *argv[])
{
    const char *error;
    int   erroffset;
    pcre *re;
    int   rc;
    int   i;
    int   ovector[100];

    char *regex = "From:([^@]+)@([^\r]+)";
    char str[]  = "From:regular.expressions@example.com\r\n"\
                  "From:exddd@43434.com\r\n"\
                  "From:7853456@exgem.com\r\n";

    re = pcre_compile (regex,          /* the pattern */
                       PCRE_MULTILINE,
                       &error,         /* for error message */
                       &erroffset,     /* for error offset */
                       0);             /* use default character tables */
    if (!re)
    {
        printf("pcre_compile failed (offset: %d), %s\n", erroffset, error);
        return -1;
    }

    unsigned int offset = 0;
    unsigned int len    = strlen(str);
    while (offset < len && (rc = pcre_exec(re, 0, str, len, offset, 0, ovector, sizeof(ovector))) >= 0)
    {
        int i;
        for(i = 0; i < rc; ++i)
        {
            printf("%2d: %.*s\n", i, ovector[2*i+1] - ovector[2*i], str + ovector[2*i]);
        }
        offset = ovector[1];
    }
    return 1;
}
