#include <string>
#include <iostream>

long long LN = 0x0000111100FFL;
std::string s = (char[6]){'t', '\0', 't', 'o', 'u', 'u' };
char xx [3] = { 'k', 'k', 'k' };

main()
{
	std::string x = "toto";
	const char y[6] = { 't', 'o', 't', 'o', '\0', 'u' };


	if (x == y) {
		std::cout << "egal\n"; 
	} else {
		std::cout << "NOT egal\n"; 
	}
	std::cout << "s=" << s << ", size=" << s.size() <<"\n";
	std::cout << "LN=" << std::hex << std::showbase << LN << "\n";
	std::cout << "sizeof(LN)=" << sizeof(LN) <<  "\n";

}
