
#include <iostream>
using namespace std;

class A {
public:
	~A() {
		cerr << "in ~A()" << endl;
		abort();
	}

};

main()
{
	static A a;
	cerr << "tototo\n";
	exit(1);
}

