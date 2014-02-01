
#include <iostream>
#include <memory>
using namespace std;

class A {
public:
	A() { cout << "constructor A\n"; }
	~A() { cout << "destructor A\n"; }
};

static A aaa;
main()
{
	cout << "start\n";
	auto_ptr<A> a;
	cout << "end\n";
}
