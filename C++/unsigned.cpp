#include <iostream>
using namespace std;

main()
{
    int i = 0x7FFFFFFF;
    short int s = i;
    cout << "i=" << i << ", s=" << s << endl;

    s = -1;
    short int s2 = 0xFFFF;
    cout << "s=" << s << ", s2=" << s2 << endl;
}

