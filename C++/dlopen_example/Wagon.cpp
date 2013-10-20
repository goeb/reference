
#include "Wagon.hpp"

Wagon::Wagon(const string & _name)
{
    name = _name;
}

void Wagon::print()
{
    cout << "Wagon::print()" << endl;
}

Wagon::~Wagon()
{
    cout << "Wagon::~Wagon()\n";
}

