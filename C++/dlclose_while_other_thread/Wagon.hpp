#ifndef __WAGON
#define __WAGON

#include <iostream>
using namespace std;

class Wagon {
    public:
    string name;
    int counter;
    Wagon(const string & _name);
    virtual ~Wagon();
    virtual void print();
    virtual void run_thread();
};

#endif
