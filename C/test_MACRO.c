
//#include <stdio.h>

#define SIGNAL2(_name, _struct) \
typedef struct _struct T##_name; \
int send_##_name(T##_name x) { \
   int i = 0;  \
}

#define SIGNAL(_s, _t1, _t2) \
int send_##_s(_t1 a1, _t2 a2) { \
	int i = 333; \
}

#define VARIABLE(_x, args...) \
>>>> _x / args

VARIABLE(1,2, 3, 4)

#define SIMPLE(_x, _y) \
void send_##_x(_y)

SIMPLE(signame, int x; int y; char *;)


SIGNAL(sig1, int, int)
SIGNAL2(sigXXX, {int x; char y[3]; })

struct T { int x; char s[10]; };

struct T xxx = { 222, "0123456789" };

main() {
	send_sig1(1, 2);
	int a = 55;
	char b[3] = "zz";
	send_sigXXX({ a, b});

}

