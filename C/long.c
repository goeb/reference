
#include <bitset>
#include <string>
#include <stdio.h>

main()
{
	long x = 252;
	unsigned long y = (long)x;
	printf("x=%ld, y=%ld\n", x, y);

	std::bitset<8> lastByteSet ((long)x);

    std::string strLastByte; // for debug
    for (int i=0; i < 8; i++) {
        if (lastByteSet[i]) strLastByte += '1';
        else strLastByte += '0';
    }
    printf("lastByte=%s", strLastByte.c_str());

	std::bitset<8> lastByteSet2(252);
	strLastByte="";
	    for (int i=0; i < 8; i++) {
        if (lastByteSet2[i]) strLastByte += '1';
        else strLastByte += '0';
    }
    printf("lastByte2=%s", strLastByte.c_str());



}

