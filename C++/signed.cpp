#include <iostream>
#include <stdint.h>

#include <string>
main()
{
	std::string bytes;
	bytes += (char) 0;
	bytes += (char) 0xFC;

	std::cout << "bytes=" << bytes << "\n";
	
	uint16_t x, y;
	x = (bytes[0] << 8) + (unsigned char )bytes[1];
	std::cout << "x=" << x << "\n";

	y = bytes[1];
	std::cout << "y=" << y << "\n";

	x = 0xFFFF;
	int a = x;
	std::cout << "a=" << a << "\n";

	uint8_t xx = 0xFF;
	char c = xx;
	std::cout << "c=" << c << "\n";
	
}
