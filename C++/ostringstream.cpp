#include <iostream>
#include <sstream>
using namespace std;

int main () {
	char str[] = "Test sentence";
	int val = 65;
	char ch = 'A';
	ostringstream s;

  	s << str << endl;     // Insert string
	s << ch << endl;      // Insert single character
	s << val << endl;
	cout << s.str();
	s.seekp(0);
	s << string("tototo\n");
	cout << s.str();
    s.str("");
    s << hex << 1048575 << "-" << dec << 123 << endl;

    cout << "s=" << s.str() << endl;
	return 0;
}
