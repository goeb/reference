#include <stdio.h>
class A 
{
    public:
        int x;
        int y;

};

A & f()
{
    static int counter = 0;
    A a;
    a.x = counter;
    counter++;
    a.y = counter;
    counter++;
    return a;
}

main() {
char s[] = "xxx toto et titi";
printf("<%s>\n", s);
unsigned int x = -1;
x++;
printf("<%d>\n", x);
A & a = f();
A a2 = f();
A a3 = f();
printf("a=%d, %d\n", a.x, a.y);

A * aa = 0;
const A * ab = 0;
A * const ac = 0;

aa = &a;
ab = &a;
ac = &a;
}
