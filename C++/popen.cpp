#include <iostream>
using namespace std;
#include <stdio.h>

main()
{
    FILE *fd;

    fd = popen("/bin/ls -l", "r");
    if (!fd)
    {
        cerr << "ERROR in popen.\n";
    }
    else
    {
        #define BUF_SIZE 1024
        char buffer[BUF_SIZE+1];
        int n = fread(&buffer, 1, BUF_SIZE, fd);
        buffer[BUF_SIZE] = 0;
        cout << "------ buffer (" << n << " bytes) ---------------" << endl;
        cout << buffer << endl;
        cout << "------- end -----------------" << endl;

        pclose(fd);
    }
}
