#include <iostream>

namespace N1 {

class A {
	int x;
};

}
namespace N2 {

class A {
	int y;
};

}

using namespace N1;
using namespace N2;

main() {
	std::cout << "hello\n";
	A a;
	
}

