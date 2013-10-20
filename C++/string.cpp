
#include <iostream>
#include <string>


//using namespace std;

main() {
	std::string s;
	s = "toto";
	std::cout << "s=" << s << std::endl;
	std::cout << "s.size()=" << s.size() << std::endl;
    s += '\0';
	std::cout << "s=" << s << ", s.size()=" << s.size() << std::endl;
    s += "yoyo";
	std::cout << "s=" << s << ", s.size()=" << s.size() << std::endl;
    s += "yoyo";

}
