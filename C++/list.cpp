#include <iostream>
#include <list>

main() {
    std::list<std::string> L;
    L.push_back("toto");
    L.push_back("titi");
    L.push_back("tutu");
    std::list<std::string>::iterator i;
    for (i=L.begin(); i!=L.end(); i++) {
        std::cout << *i << ", ";
    }
    std::cout << "\n";

    for (i=L.begin(); i!=L.end(); i++) {
        *i = (*i) + "-xx";
    }

    for (i=L.begin(); i!=L.end(); i++) {
        std::cout << *i << ", ";
    }
    std::cout << "\n";
}
