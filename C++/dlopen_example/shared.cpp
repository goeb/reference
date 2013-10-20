
#include "Wagon.hpp"

class BlueWagon : public Wagon {
    public:
    BlueWagon(const string & _name);
    virtual ~BlueWagon();
    virtual void print();
};

BlueWagon::BlueWagon(const string & _name) : Wagon(_name)
{}

BlueWagon::~BlueWagon()
{
    cout << "BlueWagon::~BlueWagon()\n";
}

extern "C"
{
    int square(int arg)
    {
        return (arg*arg);
    }

    Wagon* createWagon(string &name) {
        return new BlueWagon(name);
    }

};

void BlueWagon::print() {
    cout << "BlueWagon: my name is " << name << endl;
}



