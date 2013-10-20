
#include <iostream>
#include <fstream>

using namespace std;

main()
{
    ofstream fileHandle;
    fileHandle.exceptions(ofstream::failbit | ofstream::badbit);
    try
    {
        fileHandle.open("toto.txt", ios_base::out);
        fileHandle << "my taylor is rich. " << 444 << endl;
        fileHandle << "xxx" << endl;
    }
    catch (ofstream::failure e)
    {
        cout << "Exception opening/writing file\n";
    }
    
}
