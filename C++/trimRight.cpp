#include <stdio.h>
#include <string>
#include <string.h>

void trimRight(std::string &s, const char *c)
{
    size_t i = s.size();
    while ( (i>0) && strchr(c, s[i-1]) ) i--;

    s = s.substr(0, i);
}

void test(const char *s)
{
    std::string str;
    if (s) str = s;
    trimRight(str, " ");
    printf("[%s] => [%s]\n", s, str.c_str());
}

int main()
{
    test("");
    test("x");
    test(" x");
    test("x ");
    test("x  ");
    test("x  y");

}
