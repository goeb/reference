#include <stdio.h>

main()
{
    char s[100] = "123";
    snprintf(s, 4, "%02X", 1048575);
    printf("s=%s\n", s);
}
