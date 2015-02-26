
#include <stdio.h>

#include <fnmatch.h>

int main(int argc, char **argv)
{
    int r = fnmatch(argv[1], argv[2], 0);
    printf("r=%d\n", r);
}
