#include <stdio.h>
#include <string>
#include <iostream>
int main()
{
    std::string data;
    while (!std::cin.eof()) {
        char c;
        std::cin.read(&c, 1);
        data += c;
    }

    printf("data=[%s]\n", data.c_str());

}
