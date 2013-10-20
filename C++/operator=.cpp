#include <iostream>
using namespace std;

class A {
public:
	A & operator=(const A &x) {
		cout << "In: A:=\n";
		return *this;
	}
};

class B {
public:
	int x;
	A a;
	//B & operator=(const B &x) {
		//cout << "In: B:=\n";
		//return *this;
	//}
};

main() {
	B b, c;
	b.x = 333;
	cout << "c = b\n";
	c = b;
	cout << "c = B(b)\n";
	c = B(b);
}

