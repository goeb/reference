#include <fstream>
#include <stdio.h>

main()
{
    std::ofstream db_file("tmp.x", std::ios::out | std::ios::trunc);
    if (!db_file){
        printf("!db_file\n");
    } else printf("db_file\n");

    printf("db_file.good()=%d\n", db_file.good());


}
