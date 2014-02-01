#include <map>
#include <iostream>
#include <string>

std::map<std::string, int> SAMPLE;

const std::map<std::string, int> & getX()
{
	if (0) return SAMPLE;
}

main()
{
	SAMPLE[std::string("a")] = 11;
	SAMPLE[std::string("b")] = 12;
	SAMPLE[std::string("c")] = 13;
	std::map<std::string, int>::const_iterator i;
	for (i = getX().begin(); i != getX().end(); i++) {
		std::cout << "yy: " << i->first << ", " << i->second << "\n";
	}
	std::cout << "XXX\n";
}
