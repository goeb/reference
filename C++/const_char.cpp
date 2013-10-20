#include <iostream>
using namespace std;
char * getOne()
{
    char *p = "toto-11";
    return p;
}
char * getTwo()
{
    char *p = "titi-22";
    return p;
}

main(int argc, char **argv)
{
    const char * s;

    if (atoi(argv[1]) == 1)
    {
        s = getOne();
    }
    else
    {
        s = getTwo();
    }

    cout << "s=" << s << endl;
}
