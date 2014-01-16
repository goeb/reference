#include <stdio.h>

int f(char * &p)
{
	p = "toto";
}
main()
{
	unsigned char * p = 0;
	int x = f((unsigned char * )p);
	printf("p=%s\n", (char*)p);

}
