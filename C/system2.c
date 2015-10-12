#include <stdlib.h>
#include <stdio.h>


int main()
{
	putenv("XX=1234");
	system("echo XX=$XX; env | grep XX");
}
