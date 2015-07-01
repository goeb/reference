
#include <stdio.h>
#include <stdlib.h>

main(int argc, char ** argv)
{
    const char * s = "[my-section]";

    char *sectionName = 0;
	char buf1[100];
	char buf2[100];
	char buf3[100];
	char buf4[100];
    int n = sscanf(argv[1], argv[2], buf1, buf2, buf3, buf4);
    printf("n=%d, buf1=%s, buf2=%s, buf3=%s, buf4=%s\n", n, buf1, buf2, buf3, buf4);

}
