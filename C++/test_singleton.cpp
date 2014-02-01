#include <iostream>
using namespace std;


class A
{
    public:
    static A * singleton;
    static A* getInstance() { if (!singleton) singleton = new A(); return singleton; }
    int x;
    int y;
};

A * A::singleton = 0;

main()
{
    A* a = A::getInstance();

    a->x = 333;
    a->y = 444;
    cout << "a->x=" << a->x << ", a->y=" << a->y << endl;

    A * b = a->singleton;
    cout << "b->x=" << b->x << ", b->y=" << b->y << endl;

}
