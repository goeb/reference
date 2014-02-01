#include <stdio.h>
struct Event {
	int type;
	union {
		char s[10];
		int a;
		int b;
	};
};

main() {
	struct Event e;
	e.a = 33;
	e.type = 88;
	printf("e.b=%d, e.type=%d\n", e.b, e.type);
}
