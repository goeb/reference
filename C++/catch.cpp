#include <iostream>
using namespace std;

class A {
public:
	int x;
	void printMe() {
		x = 666;
	}
};

void g()
{
	cout << "g()\n";

	//A *a = 0;
	//a->printMe();
	
	throw 'u';
}

void f() throw (int)
{
	cout << "f()\n";

	g();
	//throw 66;
	//throw 't';
}

int main()
{

  try {
      f();
  }
  catch (const int & n) {
      cerr << "exception caught: " << n << endl;
  }
  catch (...) {
  	cerr << "UNKNOWN exception" << endl;

  }

  return 0;
}
	

