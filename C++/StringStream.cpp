
#include <sstream>
#include <stdarg.h>
#include <stdio.h>

class StringStream: public std::ostringstream {
public:
    int printf(const char *format, ...);
};


int StringStream::printf(const char *format, ...)
{
    va_list list;
    va_start(list, format);
    char *strp = NULL;
    int n = vasprintf(&strp, format, list);
    va_end(list);

    if (n >= 0) {
        (*this) << strp;
    }
    return n;
}

int main()
{
	StringStream s;
	s << "123\n";
	s.printf("%s-%s:%d\n", "hello", "world", 456);
	printf("s=%s", s.str().c_str());
}
