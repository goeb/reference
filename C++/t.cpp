
#include <iostream>
using namespace std;

void f(int & x)
{
    x++;
    usleep(100);
}

main()
{
    int x = 10;
    
    cout << "starting: x=" << x << endl;
    for (int i=0; i<1000000; i++)
    {
        f(x);
        usleep(100);
    }
    cout << "ending: x=" << x << endl;
}
