
#include <iostream>
#include <string>

int main()
{
	const std::string atcmds[3] = { "AT+1", "AT+2", "AT+3"};
	for (auto atcmd : atcmds) {
		std::cout << "atcmd=" << atcmd << std::endl;
	}


}
