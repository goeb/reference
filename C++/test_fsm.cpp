
/**
 * g++ -o test_fsm test_fsm.cpp -lpthread -g
 *
 * socat -d -v -x -lu PTY,link=ttySAAA,raw,echo=0,b19200 PTY,link=ttySBBB,raw,echo=0,b19200
 * ./test_fsm ttySAAA AAA BBB 1
 * ./test_fsm ttySBBB BBB AAA 50
 *
 * Example of output of process 1:
 * -------------------------------
 * AAA: fsm_data_req()
 * >> ping
 * AAA: fsm_data_req()
 * AAA: not READY
 * AAA: fsm_data_req()
 * AAA: not READY
 *   << pong
 * AAA received: pong
 * AAA: timeout!
 * AAA: fsm_data_req()
 * >> ping
 *   << pong
 *
 *
 */

#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <pthread.h>
#include <sys/eventfd.h>
#include <unistd.h>
#include <sys/timerfd.h>


#include <list>

enum State {
	READY,
	BUSY
};

struct Data {
	char source[6];
	char destination[6];
	char data[30];
};
// globals
enum State fsm_state = READY;

std::list<struct Data*> fsm_queue_from_user;
std::list<struct Data*> fsm_queue_to_user;
int fsm_serial = -1;
int fsm_user = -1;
int fsm_timer = -1;
const char * fsm_local_name = 0;

// FSM API functions
//
int fsm_data_req(struct Data* data)
{
	fprintf(stderr, "%s: fsm_data_req()\n", fsm_local_name);
	if (fsm_state == READY) {
		fsm_state = BUSY;
		// push into queue of pending requests
		memcpy(data->source, fsm_local_name, 6);
		fsm_queue_from_user.push_back(data);
		uint64_t x = 1;	
		write(fsm_user, &x, sizeof(uint64_t)); // notify main loop 
		return 0;
	} else {
		fprintf(stderr, "%s: not READY\n", fsm_local_name);
		return -1;
	}
}

int fsm_connect()
{
	// a user layer is connecting to fsm
	fsm_user = eventfd(0, 0);
	return fsm_user;
}

void fsm_get_indication(struct Data **msg)
{
	// called by the user layer to retrieve the message
	if (fsm_queue_to_user.empty()) *msg = 0;
	else {
		*msg = fsm_queue_to_user.front();
		fsm_queue_to_user.pop_front();
	}
}

// FSM internal functions
//
void fsm_handle_serial_indication()
{
	// read data from serial
	struct Data *data = new struct Data;
	int n = read(fsm_serial, data, sizeof(struct Data)); // TODO manage incomplete read
	// decode data, etc.
	if (n < 0) { perror("read error:"); exit(1); }
	if (n == 0) { fprintf(stderr, "read error: end-of-file\n"); exit(1); }

	fprintf(stderr, "  << %s\n", data->data);
	if (0 == strcmp("ping", data->data)) {
		// answer with pong
		strcpy(data->data, "pong");
		fprintf(stderr, ">> %s\n", data->data);
		int n = write(fsm_serial, data, sizeof(struct Data));
		if (n < 0) { perror("write error: "); exit(1); }
	} else {
		// pass it to user
		fsm_queue_to_user.push_back(data);
		// notify user TODO
	}
	fsm_state = READY;
}

void fsm_set_timer(int s)
{
	fsm_timer = timerfd_create(CLOCK_MONOTONIC, 0);
	struct itimerspec itimer;
	itimer.it_value.tv_sec = s;
	itimer.it_value.tv_nsec = 0;
	itimer.it_interval.tv_sec = 0;
	itimer.it_interval.tv_nsec = 0;
	timerfd_settime(fsm_timer, 0, &itimer, NULL);
}

void fsm_handle_user_request()
{
	struct Data *data = fsm_queue_from_user.front();
	fsm_queue_from_user.pop_front();
	fprintf(stderr, ">> %s\n", data->data);
	int n = write(fsm_serial, data, sizeof(struct Data)); // TODO manage incomplete write
	if (n < 0) { perror("write error: "); exit(1); }
	delete data;
	fsm_set_timer(3); // 3 seconds
	fsm_state = BUSY;
}

void fsm_handle_timeout()
{
	// timeout
	close(fsm_timer);
	fsm_timer = -1;
	fprintf(stderr, "%s: timeout!\n", fsm_local_name);
	fsm_state = READY;
}

void *fsm_main_loop(void*)
{
	int nfds = -1;
	fd_set rd, wr;

	fsm_state = READY;
	
	while (1) {
		FD_ZERO(&wr);
		FD_ZERO(&rd);
		FD_SET(fsm_serial, &rd);
		FD_SET(fsm_user, &rd);
		if (fsm_timer >= 0) FD_SET(fsm_timer, &rd);
		nfds = fsm_user;
		if (fsm_serial > fsm_user) nfds = fsm_serial;
		if ( (fsm_timer >= 0) && (fsm_timer > fsm_serial) ) nfds = fsm_timer;

		int status = pselect(nfds + 1, &rd, &wr, 0, 0, 0);
		//fprintf(stderr, "pselect status: %d\n", status);
		if (-1 == status) {
			if (errno != EINTR) {
				// error
				perror("error in pselect:");
				exit(1);
			} else continue;
		} else {
			// find out which handle is concerned
			if (FD_ISSET(fsm_serial, &rd)) {
				fsm_handle_serial_indication();
			}

			if (FD_ISSET(fsm_user, &rd)) {
				fsm_handle_user_request();
				uint64_t x;
				read(fsm_user, &x, sizeof(uint64_t));
			}

			if (FD_ISSET(fsm_timer, &rd)) {
				fsm_handle_timeout();
			}
		}
	}
}


void fsm_init(const char *device, const char * local_name) 
{
	// open serial port
	fsm_serial = open(device, O_RDWR);
	fsm_local_name = local_name;

	// start main loop in separate thread
	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_t t;
	pthread_create(&t, &attr, fsm_main_loop, (void*)0);
}

int main(int argc, char **argv)
{
	// usage: test_fsm <device> <name> <remote> <period>
	const char * local_name = argv[2];
	fsm_init(argv[1], local_name);
	int fsm_layer = fsm_connect();
	
	int t = 0;
	int period = atoi(argv[4]);
	while (1) {
		if (t > period*10) {
			// send user data
			struct Data *data = new struct Data;
			memcpy(data->destination, argv[3], 6);
			strcpy(data->data, "ping");
			fsm_data_req(data);
			t = 0;
		}
		// check if data indication
		struct Data *data;
		fsm_get_indication(&data);
		if (data) {
			fprintf(stderr, "%s received: %s\n", local_name, data->data);
			delete data;
		}
		usleep(100000);
		t++;
		
	}
}
