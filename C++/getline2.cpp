#include <iostream>
#include <string>
#include <fstream>
#include <errno.h>
#include <string.h>
#include <unistd.h>

int main(int arc, char **argv)
{
    std::string line;
    std::ifstream infile;
    infile.open(argv[1]); // open file
    if (infile) {
        while (getline(infile, line)) {
            std::cout << "line: " << line << std::endl;
            sleep(2);
        }
        if (infile.bad()) {
            std::cerr << "badbit: "  << strerror(errno) << std::endl;
        }

    } else std::cerr << "cannot open file: " << argv[1] << ": " << strerror(errno) << std::endl;
    return 0;
}   

