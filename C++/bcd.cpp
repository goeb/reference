#include <sstream>
#include <stdio.h>
main() 
{

	std::stringstream ss;
	std::string a = "274345640000054e";

	// old style (wrong)
	short byte;
	for (int i = 0; i < a.size()/2; i++) {
		std::stringstream ss;
		ss << a.substr(2*i,2);
		ss >> byte; // FOB.12926 TODO ?
		printf("byte=%x\n", byte);
	}

	// bcd
	int firstNibble = -1;
	unsigned char byte2 = 0;
	for (int i = 0; i < a.size(); i++) {
		char c = a[i];
		if (c < '0' || c > '9') {
			printf("error: c=%x\n", c);
		}
		if (firstNibble < 0) {
			firstNibble = c - '0';
		} else {
			byte2 = (firstNibble << 4) + (c - '0');
			firstNibble = -1;
			printf("byte2=%x\n", byte2);
		}
	}


}
