#include <string.h>
#include <stdio.h>

main() {
	char *s = "123";
	char t[10] = "";
	strncpy(t, s, 3);
	strncat(t, s, 3);
	printf("%s\n", t);
}
