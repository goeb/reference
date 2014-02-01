#include <iostream>

main()
{
	std::string s = "";
	s += '\0';
	s += 'x';
	std::cout << "s.size()=" << s.size() << std::endl;

	std::string s2 = "";
	s2 += s[0];
	s2 += s[1];

	std::cout << "s2.size()=" << s2.size() << std::endl;
}
