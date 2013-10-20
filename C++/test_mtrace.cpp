#include <iostream>
using namespace std;
#include <mcheck.h>
#include <stdlib.h>


/*
MALLOC_TRACE=/home/YourUserName/path/to/program/MallocTraceOutputFile.txt
export MALLOC_TRACE;
*/

class A
{
    public:
    int x;
    string s;
};

void f()
{
    A *a = new A();
    //char * x = (char *) malloc (255);
    char *x = new char[0xFFFF];
}

main()
{
    mtrace();
    A *a = new A();
    a->x = 33;
    a->s = "tototo---+++";
    delete a;
    f();

}
