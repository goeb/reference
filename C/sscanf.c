#include <stdio.h>

main()
{
    const char * s = "[my-section]";

    char *sectionName = 0;
    int n = sscanf(s, "[%sa]", sectionName);
    printf("n=%d, sectionName=%s\n", n, sectionName);
}
