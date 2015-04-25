#include <stdio.h>

const char *reservedNames[] = {
    "views",
    "issues",
    "files",
    "public",
    0
};

int main() {
    const char **ptr = reservedNames;
    while (*ptr) {
        printf("=> %s\n", *ptr);
        ptr++;
    }
}
