/*
 * Simple example of a program that communicates with a ME
 * (Mobile Equipment, being a modem) with AT commands.
 *
 * The ME is simulated by the user and his/her keyboard.
 *
 *
 */
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <poll.h>
#include <unistd.h>
#include <sys/types.h>
#include <string>

enum RecvState {
	READY,   // ready to receive URC or send an AT commmand
	AT_RESP  // A response to an AT command is being received
};

#define AT_CREG "AT+CREG?"

RecvState parse_line(const std::string &line, RecvState state, const char *current_at_cmd)
{
	switch (state) {
		case READY:
			if (current_at_cmd && line == current_at_cmd) state = AT_RESP;
			else state = READY;
			break;
		case AT_RESP:
			if (line == "OK" || line == "ERROR") state = READY;
			break;
	}
	fprintf(stderr, "state %s\n", state==READY?"READY":"AT_RESP");
	return state;
}

void main_loop()
{
    fprintf(stderr, "main_loop...\n");
    struct pollfd ufds[1];
    ufds[0].fd = 0; // stdin
    ufds[0].events = POLLIN;

	std::string line;
	RecvState state = READY;
	const char *current_at_cmd = 0;

    while (1) {

        int rv = poll(ufds, 1, 5000); // 5 second timeout

        if (rv == -1) {
            perror("poll");
			exit(1);

        } else if (rv == 0) {
            fprintf(stderr, "Timeout occurred, send an AT command\n");
			current_at_cmd = AT_CREG;
			write(1, current_at_cmd, strlen(current_at_cmd));
			write(1, "\r\n", 2);

        } else {

            if (ufds[0].revents & POLLIN) {
				// some bytes received.
				// read one at a time (for simplicity)
				char byte;
                int n = read(0, &byte, 1);

				if (n < 0) {
					perror("read");
					exit(1);

				} else if (n == 0){
					// end of stream
					fprintf(stderr, "end.\n");
					exit(0);

				} else {
					if (byte == '\n' || byte == '\r') {
						// end of line
						state = parse_line(line, state, current_at_cmd);
						line.clear();
					} else line += byte;
				}

            }
        }
    }
}

int main()
{
    main_loop();
}
