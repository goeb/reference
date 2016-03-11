/*
 * This example, combined with constructor.mk
 * shows that a static member duplicated in 2 compilation units
 * gets initialized twice.
 *
 * Result of execution:
 * A() / 0x8049b3d
 * A() / 0x8049b3d
 * main...
 * A::printMyAddress() / 0x8049b3d
 * main completed.
 * ~A() / 0x8049b3d
 * ~A() / 0x8049b3d
 * 
 */

#include <stdio.h>

class A {
	public:
	A() { printf("A() / %p\n", this); }
	~A() { printf("~A() / %p\n", this); }

	void printMyAddress() { printf("A::printMyAddress() / %p\n", this); }
	static A StaticA;
};

A A::StaticA;

#ifdef WITH_MAIN
int main()
{
	printf("main...\n");

	A::StaticA.printMyAddress();	

	printf("main completed.\n");
}
#endif
