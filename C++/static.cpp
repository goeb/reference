#include <stdio.h>

class B
{
    public:
    B() { printf("B()\n"); }
};

class A
{
    static B b;
};

B A::b;

main()
{
    printf("main\n");
}
