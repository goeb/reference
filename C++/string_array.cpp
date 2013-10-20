#include <iostream>
#include <set>
using namespace std;

string s = "toto";

string sTab[2] = { "xABC", "yUVW", "---" };

int main()
{
    int i=0;
    //while (sTab[i] != "---")
    while (i<8)
    {
        cout << "sTab[" << i << "]=" << sTab[i] << endl;
        i++;
    }
    cout << "done.\n";

    return 0;
}

