#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>

void test_twos_complement(unsigned char *bytes, int expected)
{
	unsigned char buffer[4];
	size_t len = 4; // we work on 4 bytes
	memcpy(buffer, bytes, 4);
	for (int i=0; i<len; i++) {
		buffer[i] = 0xff - buffer[i]; // flip bits
	}
    // add 1 and handle the carry
    int carry = 1;
    for (int i=len-1; i>=0; i--) {
        buffer[i] += carry;
        if (buffer[i] == 0x00) carry = 1;
        else break; // no more carry
    }
	uint32_t *int_b = (uint32_t*)buffer;

	uint32_t r = ntohl(*int_b);
	uint32_t *origin_b = (uint32_t*)bytes;
	uint32_t origin = ntohl(*origin_b);
	printf("test_twos_complement: result=-%d, expected=%d (origin=%d)\n", r, expected, origin);
}

int main()
{
	test_twos_complement("\xFF\xFF\xFF\xFF", -1);
	test_twos_complement("\xFF\xFF\xFF\xFE", -2);
	test_twos_complement("\x80\x00\x00\x00", -2147483648);
	test_twos_complement("\x80\x00\x00\x01", -2147483647);
	test_twos_complement("\x80\x00\x00\x02", -2147483646);
}
