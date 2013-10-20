
#include <sys/vfs.h>
#include <iostream>
using namespace std;

main()
{
    struct statfs bStatFs;
    statfs("/", &bStatFs);
    cout << bStatFs.f_bsize << "," << bStatFs.f_blocks << "," << bStatFs.f_bfree << "," << bStatFs.f_bavail << endl;
}
