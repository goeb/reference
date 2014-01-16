
#include <stdio.h>
#include <math.h>

int main() {
	float a;
	for (a = 0.0; a <= 8; a+= 0.2 ) {
		int n = sin(a) * 20 + 21;
		int i;	
		printf("    ");
		for (i=0; i<n; i++) printf("x");
		printf("\n");
	}
	return 0;
}
