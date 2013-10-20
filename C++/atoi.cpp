
#include <iostream>
using namespace std;

main()
{
    char *toto = new char[15];
    char *str = "FFFF";
    long x = strtol(str, (char **)NULL, 16);
    cout << "strtol(" << str << ")=" << x << endl;

    toto[1] = 'x';
    toto[22] = 'y';
    cout << "x=" << toto[1] << endl;
    cout << "y=" << toto[22] << endl;
}

