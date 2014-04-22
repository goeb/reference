#include <stdio.h>
struct Event {
	int type;
	union {
		char s[10];
		int a;
		int b;
	};
	union {
		int u1;
		int u2;
	} uuuu;
};

main() {
	struct Event e;
	e.a = 33;
	e.type = 88;
	printf("e.b=%d, e.type=%d\n", e.b, e.type);
	e.uuuu.u1 = 444;
	e.uuuu.u2 = 555;
	printf("e.u1=%d, e.u2=%d\n", e.uuuu.u1, e.uuuu.u2);
}
