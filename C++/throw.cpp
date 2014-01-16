


// exceptions
#include <iostream>
using namespace std;

void f() {
	cout << "f()\n";
	throw "xxx";
}

int main () {
  try {
	f();
    throw 20;

  } catch (int e) {
    cout << "An exception occurred. Exception Nr. " << e << endl;

  } catch (...) {
	cout << "Other exception...\n";

  }

  return 0;
}
