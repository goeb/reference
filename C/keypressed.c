#include <stdlib.h>
#include <stdio.h>
#include <termios.h>
#include <string.h>

struct termios stored_settings;
int termios_set = 0;
void set_keypress(void) {
	struct termios new_settings;

	if (0==termios_set) {
		tcgetattr(0, &stored_settings);
		new_settings = stored_settings;
		/* Disable canonical mode, and set buffer size to 1 byte */
		new_settings.c_lflag &= (~ICANON);
		new_settings.c_cc[VTIME] = 0;
		new_settings.c_cc[VMIN] = 1;
		new_settings.c_lflag &= (~ECHO);
		tcsetattr(0, TCSANOW, &new_settings);
		termios_set = 1;
	}
	return;
}

void reset_keypress(void) {
	if (1==termios_set) {
		tcsetattr(0, TCSANOW, &stored_settings);
	}
	return;
}

int main(void) {
	char c;

	set_keypress();
	while (1) {
		c = getchar();	
		printf("<%c>\n", c);
		if ('q'==c) break;
	}
	printf("Exiting...\n");
	reset_keypress();
	return 0;
}
