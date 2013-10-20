#ifndef __SEPARATE_HPP
#define __SEPARATE_HPP

#include <iostream>
using namespace std;

#ifndef PRIVATE_MEMBERS
#define PRIVATE_MEMBERS
#endif

class A {

public :

	int x;
	string s;

	A();
	void print_my_name();

	private:

	PRIVATE_MEMBERS

};

#endif
