#ifndef __WAGON
#define __WAGON

#include <iostream>
using namespace std;

class Wagon {
    public:
    string name;
    Wagon(const string & _name);
    virtual ~Wagon();
    virtual void print();
};

#endif
