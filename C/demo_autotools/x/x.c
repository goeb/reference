#include <stdio.h>

int main(int argc, char **argv)
{
	printf("x\n");
#ifdef WITH_CURL
	printf("x: WITH_CURL\n");
#endif
}
