#include <stdarg.h>

typedef struct {
    int x;
    int y;
} Type1;

void eprint(int n, ...) {
    va_list     list;
    int         i, value;
    Type1       s;

    if (n<=0) return;

    va_start(list, n);
    //for (i=0; i<n; i++) {
    i=0;
    value = va_arg(list, int);
    printf("arg[%d]=%d\n", i, value);
    //}
    //
    i++;
    s = va_arg(list, Type1);
    printf("arg[%d]={%d, %d}\n", i, s.x, s.y);
    va_end(list);
}

main() {
    Type1 my_struct;
    my_struct.x = 55;
    my_struct.y = 99;
    eprint(2, 111, my_struct);
    //eprint(5, 61, 61, 63, 64, 65);
}
