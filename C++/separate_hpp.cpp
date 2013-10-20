
#define PRIVATE_MEMBERS \
	int y;

#include "separate_hpp.hpp"


A::A()
{
	y = 0;
}

void A::print_my_name() {
	cout << "A::print_my_name() / y=" << y << endl;
	y++;
}

main()
{
	A a;
	a.print_my_name();
	a.print_my_name();
	a.print_my_name();
}

