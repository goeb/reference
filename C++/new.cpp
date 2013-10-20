#include <iostream>
using namespace std;

class MyClass {
public:
	int i;
	MyClass(void) {
		i = 0;
	}

};
main() {
	MyClass *c;
	c = new MyClass();
	if (c == NULL) {
		cout << "trace: pointer=" << c << "\n";
	} else  {
		cout << "trace: pointer=" << c << "\n";

	}
}
