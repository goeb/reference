#include <stdio.h>
#include <string.h>
class A {
public:
	int id;
	char name[30];
};

class B : public A {
public:
	B(A a) { id = a.id; strcpy(name, a.name); }
	int bId;
	char bName[10];
};

main() 
{
	A a;
	a.id = 666;
	strcpy(a.name, "toto");

	B b = a;

	printf("a.id=%d, a.name=%s\n", a.id, a.name);
	printf("b.id=%d, b.name=%s\n", b.id, b.name);
}
