#define HAVE_STRLCPY

#include <strings.h>

main()
{
    char x[100];
    strlcpy(x, "toto", 100);
}
