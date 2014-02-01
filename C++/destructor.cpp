
#include <stdio.h>

class A {
public:
	virtual ~A() { printf("~A()\n"); }
	A() { printf("A()\n"); }
};
class B : public A {
public:
	~B() { printf("~B()\n"); }
	B() { printf("B()\n"); }
};

main() {
	printf("startup.\n");
	//A a;
	printf("mid.\n");
	B b;
	printf("end.\n");
}
