#include <vector>
#include <string>
#include <stdio.h>

template <class T> class A
{
public:
	T x;
};

template <typename T> std::vector<T> shuffle(const std::vector<T> &L, bool &x)
{
    std::vector<T> xx;
    return x;
}

class B {
    public:
        template <typename T> std::vector<T> shuffle(const std::vector<T> &L, bool &x) {
            std::vector<T> xx;
            return x;
        }
        template <typename T> static std::vector<T> shufflestatic(const std::vector<T> &L, bool &x) {
            std::vector<T> xx;
            return x;
        }
};


main()
{
	A<int> a1;
	A<char *> a2;
	a1.x = 333;
	a2.x = (char*)"tututu";
	printf("a1.x=%d, a2.x=%s", a1.x, a2.x);

}
