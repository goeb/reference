#include <iostream>

struct Object {
    float first;
    int second;
};
 
Object scalar = {0.43f, 10}; //One Object, with first=0.43f and second=10

main() {
	std::cout << scalar.first << ", " << scalar.second << "\n";
}
