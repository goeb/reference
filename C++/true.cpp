#include <iostream>
#include <sstream>
using namespace std;

main()
{
    ostringstream oss;
    oss << true;
    cout << oss.str() << endl;
}
