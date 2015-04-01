#include <iostream>
#include <sstream>
#include <stdint.h>
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
	s << 0 << endl;
	uint8_t x = 0;
	uint16_t y = 0;
	s << "x=" << (int)x << ", y=" << y << endl;

    cout << "s=" << s.str() << endl;
	return 0;
}
