#include <stdio.h>

main()
{
    const char * s = "[my-section]";

    char *sectionName = 0;
    int n = sscanf(s, "[%sa]", sectionName);
    printf("n=%d, sectionName=%s\n", n, sectionName);

    s = "Content-Disposition: form-data; name=\"file\"; filename=\"accum.png\"";
    char x[1024];
    char y[1024];
    char fname[1014];
    n = sscanf(s, "Content-Disposition: %*s %*s filename=\"%1023[^\"]", x, y, fname);
    printf("n=%d, x=%s, y=%s, fname=%s\n", x, y, fname);
}
