#include <stdio.h>
#include <iostream>
#include <time.h>

main() {
	int i;
	unsigned int ui;
	long l;
	unsigned long ul;
	long long ll;
	unsigned long long ull;
	time_t t;

	printf("sizeof(i)=%d\n", sizeof(i));
	printf("sizeof(ui)=%d\n", sizeof(ui));
	printf("sizeof(l)=%d\n", sizeof(l));
	printf("sizeof(ul)=%d\n", sizeof(ul));
	printf("sizeof(ll)=%d\n", sizeof(ll));
	printf("sizeof(ull)=%d\n", sizeof(ull));
	printf("sizeof(t)=%d\n", sizeof(t));


	int j, k;
	unsigned int uj, uk;
	j = 0;
	uj = 0;
	j--;
	uj--;
	std::cout << "j=" << j << "\n";
	std::cout << "uj=" << uj << "\n";
	j = 2147483648; // 2^31
	std::cout << "j=" << j << " (2^31)\n";
	j--;
	std::cout << "j=" << j << " (2^31-1)\n";
	j+=2;
	std::cout << "j=" << j << " (2^31+1)\n";

}
