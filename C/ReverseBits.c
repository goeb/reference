void ReverseBits(unsigned char *source, unsigned char *destination, int len)
{
	int byte_counter, bit_counter;
	unsigned char destination_byte, source_byte;
	for (byte_counter=0; byte_counter<len; byte_counter++) {
		destination_byte = 0;
		source_byte = source[byte_counter];
		for (bit_counter=0; bit_counter<8; bit_counter++) {
			destination_byte = (destination_byte << 1) + (source_byte & 0x1);
			source_byte >>= 1;
		}
		destination[byte_counter] = destination_byte;
	}
}
main()
{
	unsigned char source[5]={ 0x1, 0xFF, 0xC, 0x13, 0xE2 };
	unsigned char destination[5];
	int i;
	ReverseBits(source, destination, 5);
	for (i=0; i<5; i++) {
		printf("%02x -> %02x\n", source[i], destination[i]);
	}
}
