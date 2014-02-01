#include <stdint.h>
#include <stdio.h>

#define HL_MAJOR(_x) ( (_x & 0xFF000000) >> 24 )
#define HL_MINOR(_x) ( (_x & 0xFFFF00) >> 8 )
#define HL_PATCH(_x) ( _x & 0xFF )

int main()
{
	uint32_t x = 0x12345678;
	printf("%x.%x.%x\n", HL_MAJOR(x), HL_MINOR(x), HL_PATCH(x));
}

