#include <iostream>
#include "stub.hpp"

void stubA::f(void) {
	std::cout << "stuba::f()\n";
}

main() {
	stubA a;
	a.f();
}
