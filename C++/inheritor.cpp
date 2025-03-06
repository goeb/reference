#include <stdio.h>

class A {
    public:
    A()  { printf("A()\n"); }
    ~A() { printf("~A()\n"); }
	A& operator=(const A&) { printf("A=()\n"); return *this; }
};

class B : public A {
    public:
    B() { printf("B()\n"); }
    ~B() { printf("~B()\n"); }
	B& operator=(const B&) { printf("B=()\n"); return *this; }
};

int main() {
    A* a = new A(); // calls A()
    delete a;       // calls ~A()
    B* b = new B(); // calls A(), then B()
    delete b;       // calls ~B() then ~A()
	a = new B();    // calls A(), then B()
	delete a;       // calls only ~A(), because ~A() is not virtual

	// Test operator=
	A a1, a2;
	a1 = a2;         // calls A=()
	B b1, b2;
	b1 = b2;         // calls B=()
	A* a3 = new B();
	(*a3) = a2;      // calls A=()
	delete a3;

	return 0;
}

