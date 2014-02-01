#include <iostream>
#include <string>

main()
{
	std::string s = "123456789";
	std::cout << "s=" << s << std::endl;

	std::string s2;
	s2 = s.substr(2, 3);
	std::cout << "s2=" << s2 << std::endl;

	std::string s3 = "123";
	try {
		s3.substr(3, 1);
		std::cout << "123.substr(3, 1) : ok\n";
	} catch (...) {
		std::cout << "123.substr(3, 1) : exception\n";
	}

	try {
		s3.substr(4, 1);
		std::cout << "123.substr(4, 1) : ok\n";
	} catch (...) {
		std::cout << "123.substr(4, 1) : exception\n";
	}

	// throw 
	//terminate called after throwing an instance of 'std::out_of_range'
	//what():  basic_string::substr
	//Aborted

	//s2 = s.substr(20, 3);
	//std::cout << "s2=" << s2 << std::endl;

	size_t index = s.find('9');
	s2 = s.substr(index+2);
	std::cout << "s2=" << s2 << std::endl;

}
