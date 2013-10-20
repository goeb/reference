#include <iostream>
//#include <exceptions>

class A {
public:
	A() {
		std::cout << "in default constructor\n";
	}

	~A() {
		std::cout << "in destructor A\n";
		throw 999;
	}

};

main() {
	std::cout << "hello\n";
	try {
		{
			A a;
			std::cout << "1.\n";
		}
		std::cout << "end try.\n";
	}
	catch (int e) {
		std::cout << "catch !!\n";
	}
	std::cout << "2.\n";

}
