#include <iostream>
#include <sstream>
main()
{
	std::ostringstream s;

std::cout << "\t\t\t<< comm ok IC:" << std::showbase << std::hex << 255
						<< " CC:" <<255
						<< " DC:" << 255
						<< std::endl;
s << "x: " << std::hex << std::showbase << "a=" << 255
						<< " CC:" <<255
						<< " DC:" << 255
						<< "\n";
s << "y: " << 33  << "\n";
s << "z: " << 0  << "\n";
std::cout << s.str();
}
