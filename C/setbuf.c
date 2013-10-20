
#include <stdio.h>
#include <unistd.h>

main()
{
    setvbuf(stdout, 0, _IONBF, 0);
    printf("toto\n");
    printf("titi\n");
    fprintf(stderr, "KIKI \n");

    sleep(100);
    printf("tutu\n");
}
