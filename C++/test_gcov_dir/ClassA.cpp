
#include <iostream>
#include "ClassA.hpp"

static A my_static_a;

	void A::run (void) {
		std::cout << "ClassA.run()\n";
	}

extern "C" void hello() {
    std::cout << "hello" << '\n';
    std::cout << "hello" << '\n';
    std::cout << "hello" << '\n';
    std::cout << "hello" << '\n';
    std::cout << "hello" << '\n';
}

void tototo(int i) {
	std::cout << "i=" << i;

	// tototo
}

void yyyyy() {
	std::cout << "uuuu\n";
	std::cout << "tttt\n";
}
