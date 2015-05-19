#include <stdlib.h>
#include <stdio.h>


int main()
{
	FILE *f1 = fopen("system.c", "r");
	FILE *f2 = fopen("system.c", "r");
	system("ls -al /proc/self/fd");
}
