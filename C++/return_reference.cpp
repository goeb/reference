#include <iostream>
using namespace std;

class MyClass {
public:
	int i;
	MyClass(void) {
		i = 0;
	}

};

int& f() {
	int i = 33;
	return i;
}
main() {
	int y;
	{
	int x;
	x = f();
	cout << "x=" << x << endl;
	y = x;
	}
	cout << "y=" << y << endl;
}
