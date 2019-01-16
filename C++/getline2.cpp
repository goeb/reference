#include <iostream>
#include <string>
#include <fstream>
#include <errno.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char **argv)
{
    std::string line;
    std::istream *is;
    std::ifstream infile;

    if (argc > 1) {
        infile.open(argv[1]); // open file
        is = &infile;
    } else {
        is = &std::cin;
    }

    if (*is) {
        while (getline(*is, line)) {
            std::cout << "line: [" << line << "]" << std::endl;
            sleep(2);
        }
        if (is->bad()) {
            std::cerr << "badbit: "  << strerror(errno) << std::endl;
        }

    } else std::cerr << "cannot open file: " << argv[1] << ": " << strerror(errno) << std::endl;
    return 0;
}   

