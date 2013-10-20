#include <iostream>
using namespace std;

class A {
public:
	int x;
	int y;
	A & operator=(const A &a) {
		cout << "In: A:=\n";
		x = a.x;
		return *this;
	}
};

main() {
	A a, b;
	a.x = 444;
	a.y = 5555;
	b = a;
	cout << "b.x=" << b.x << ", b.y=" << b.y << "\n";
}

