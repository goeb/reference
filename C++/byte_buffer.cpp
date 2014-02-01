

#include <string>
#include <iostream>
#include <stdint.h>

typedef std::basic_string<uint8_t> buffer; 

main()
{
	buffer bytes;
	bytes += (uint8_t) 'a';
	bytes += (uint8_t) 'b';
	bytes += (uint8_t) 'c';
	uint8_t x = bytes[1];
}
