#include <string.h>

struct A_t {
    char x;
    char y;
	int z;
} A;

struct B_t {
    char xx;
    struct A_t yy;
    struct A_t zz;
} B;

main() {
    printf("sizeof(A)=%d\n", sizeof(A));
    printf("sizeof(B)=%d\n", sizeof(B));
	struct A_t a;
	memset((void *)&a, 0, sizeof(a));
	int *x = &(a.z);

    printf("x=%d\n", *x);

	int *y = (int*)&(a.y);

    printf("y=%d\n", *y);
}

