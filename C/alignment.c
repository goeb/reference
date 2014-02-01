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
}

