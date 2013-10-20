#include <iostream>


void *malloc(size_t size)
{
    static int c = 0;
    static char memory[10000];
    printf("malloc(%d)\n", size);
    char * current = memory + c;
    c+=size;
    return current;
}

main()
{
    std::string s;
    printf("sizeof(s)=%d\n", sizeof(s));

    s = "toto";
    printf("sizeof(s)=%d\n", sizeof(s));
    printf("s=%s\n", s.c_str());

    char *s2 = (char*)malloc(100);
    strcpy(s2, "yoyoyo");

    std::cout << "strdup..." << std::endl;
    strdup(s2);

    std::cout << "strdup..." << std::endl;
    char *s3 = strdup(s2);

}
