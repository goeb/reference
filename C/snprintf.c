#include <stdio.h>
#include <iostream>
#include <string>

int main()
{
	const char* data = "12345";
	int length = 6;
        int i = 0;
    std::string result = "";
    for (i=0; i<length; i++) {
        unsigned char c = data[i];
        char hexaNotation[2+1];
        snprintf(hexaNotation, 3, "%02X", c);
        printf("hexaNotation[%d]=%s\n", i, hexaNotation);
        result += hexaNotation;
    }
    printf("hexaNotation: result=%s\n", result.c_str());
}

