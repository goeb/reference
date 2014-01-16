#include <stdio.h>

template <class T> class A
{
public:
	T x;
};

main()
{
	A<int> a1;
	A<char *> a2;
	a1.x = 333;
	a2.x = "tututu";
	printf("a1.x=%d, a2.x=%s", a1.x, a2.x);

}
