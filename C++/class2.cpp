#include <stdio.h>


class A {
public:
	virtual void f() { printf("virtual void A::f()\n"); }
};

class B : public A {
public:
	//virtual void f();
	void f() { printf("void B::f()\n"); }
};


int main()
{
	A a;
	B b;
	a.f();
	b.f();
	A* pa;
	pa = dynamic_cast<A*>(&b);
	pa->f();
}
