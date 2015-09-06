#include <stdio.h>

int main() {
    int tmp = 10;
    while (tmp--) {
        printf("R1/tmp=%d\n", tmp);
    }
    // start from 0
    tmp = 0;
    while (tmp--) {
        printf("R2/tmp=%d\n", tmp);
    }

}
