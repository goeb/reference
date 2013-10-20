#include <unistd.h>

#include "Wagon.hpp"

Wagon::Wagon(const string & _name)
{
    name = _name;
    counter = 0;
}

void Wagon::run_thread()
{
    cout << "Wagon::run_thread()" << endl;
    while (1)
    {
        cout << "Wagon::run_thread(): counter=" << counter << endl;
        counter++;
        usleep(200000);
    }
}

void Wagon::print()
{
    cout << "Wagon::print()" << endl;
}

Wagon::~Wagon()
{
    cout << "Wagon::~Wagon()\n";
}

