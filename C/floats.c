
#include <stdio.h>

void display_float(double x) {
	int i;
	for (i=0; i<8; i++) { // 8 is sizeof(double)
		unsigned char c;
		c = ((char *)(&x))[i];
		printf("%x-", c);
	}
	printf("\n");
}

main() {

	double a = 800.0 ;
	double b = 0.75 ;
	double c = 0.6 ;

	printf("sizeof(double)=%d\n", sizeof(double));
	printf("a=%f\n", a);
	display_float(a);

	printf("b=%f\n", b);
	display_float(b);
	printf("c=%f\n", c);
	display_float(c);

}
