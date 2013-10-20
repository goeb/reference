#include <iostream>
using namespace std;

class A {
    public:
    A() {
        cout << "A()" << endl;
    }
    ~A() {
        cout << "~A()" << endl;
    }
};

class B : public A
{
    public:
    B() {
        cout << "B()" << endl;
    }
    ~B() {
        cout << "~B()" << endl;
    }
};
main() {
    A* a = new A();
    delete a;
    B* b = new B();
    delete b;
}

