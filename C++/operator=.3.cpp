#include <iostream>
using namespace std;

class A
{
    public:
    int x;
};

class B : public A 
{
    public:
    int y;
    B& operator=(const B& other)
    {
        cout << "B::operator=" << endl;
        A::operator=(other);
        y = other.y;
        return *this;
    }
};

main()
{
    B b1;
    B b2;
    b1.x = 33;
    b1.y = 44;
    b2 = b1;
    cout << "b1.x=" << b1.x << ", b1.y=" << b1.y << endl;
    cout << "b2.x=" << b2.x << ", b2.y=" << b2.y << endl;
}
