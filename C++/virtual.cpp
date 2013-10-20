#include <iostream>
using namespace std;

class A {
public:
	void f() { cout << "A:f()\n"; g(); }
	virtual void g() = 0;
};

class B : public A {
public:
	
	virtual void g() { cout << "B:g()\n"; };
};

main() {
	A *a;
	B b;
	b.f();
	a = (A*)&b;
	a->f();
};
