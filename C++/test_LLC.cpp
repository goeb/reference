
/**
 * g++ -o  test_LLC test_LLC.cpp -lpthread -g
 *
 * socat -d -v -x -lu PTY,link=ttySAAA,raw,echo=0,b19200 PTY,link=ttySBBB,raw,echo=0,b19200
 * ./test_LLC ttySAAA AAA BBB 1
 * ./test_LLC ttySBBB BBB AAA 50
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


class LlcLayer
{
public:
					// LLC API functions
					LlcLayer();
	void			Init(const char *device, const char * localName);
	int				Connect();
	int				DataReq(struct Data* data);
	void			GetIndication(struct Data **msg);
	std::string		GetPing();
	
private:
	// methods
	void HandleSerialIndication();
	void HandleTimeout();
	void HandleUserRequest();
	void StartTimer(int s);
	void StopTimer();
	void *MainLoop();
	static void *	MainLoopStatic(void *);

	// members
	int serialFd;
	int userFd;
	int timerFd;
	const char * localName;
	std::list<struct Data*> RequestQueueFromUser;
	std::list<struct Data*> IndicationQueueToUser;
	enum State state;
	int pendingPibRequestFd;
	char * pendingPibRequest;
};

LlcLayer::LlcLayer()
{
	state = READY;
	serialFd = -1;
	userFd = -1;
	timerFd = -1;
	localName = "none";
}

void LlcLayer::Init(const char *device, const char * name) 
{
	// open serial port
	serialFd = open(device, O_RDWR);
	localName = name;

	// start main loop in separate thread
	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_t t;
	pthread_create(&t, &attr, MainLoopStatic, (void*)this);
}

int LlcLayer::DataReq(struct Data* data)
{
	fprintf(stderr, "%s: LlcLayer::DataReq()\n", localName);
	if (state == READY) {
		state = BUSY;
		// push into queue of pending requests
		memcpy(data->source, localName, 6);
		RequestQueueFromUser.push_back(data);
		uint64_t x = 1;	
		write(userFd, &x, sizeof(uint64_t)); // notify main loop 
		return 0;
	} else {
		fprintf(stderr, "%s: not READY\n", localName);
		return -1;
	}
}

int LlcLayer::Connect()
{
	// a user layer is connecting to fsm
	int x = eventfd(0, 0);
	userFd = eventfd(0, 0);
	return x;
}

void LlcLayer::GetIndication(struct Data **msg)
{
	// called by the user layer to retrieve the message
	if (IndicationQueueToUser.empty()) *msg = 0;
	else {
		*msg = IndicationQueueToUser.front();
		IndicationQueueToUser.pop_front();
	}
}

std::string LlcLayer::GetPing()
{
	struct Data *data = new struct Data;
	memcpy(data->destination, "XXX", 6);
	strcpy(data->data, "ping");

	int x = fsm.DataReq(data); // push into queue
	if (x < 0) return x;

	// else wait until request got a response
	pendingPibRequestFd = eventfd(0, 0);
	int n = read(pendingPibRequestFd
	
}

// FSM internal functions
//
void LlcLayer::HandleSerialIndication()
{
	// read data from serial
	struct Data *data = new struct Data;
	int n = read(serialFd, data, sizeof(struct Data)); // TODO manage incomplete read
	// decode data, etc.
	if (n < 0) { perror("read error:"); exit(1); }
	if (n == 0) { fprintf(stderr, "read error: end-of-file\n"); exit(1); }

	fprintf(stderr, "  << %s\n", data->data);
	if (0 == strcmp("ping", data->data)) {
		// answer with pong
		strcpy(data->data, "pong");
		fprintf(stderr, ">> %s\n", data->data);
		int n = write(serialFd, data, sizeof(struct Data));
		if (n < 0) { perror("write error 1: "); exit(1); }
	} else {
		// pass it to user
		IndicationQueueToUser.push_back(data);
		// notify user TODO
	}
	state = READY;
}

void LlcLayer::StartTimer(int s)
{
	timerFd = timerfd_create(CLOCK_MONOTONIC, 0);
	struct itimerspec itimer;
	itimer.it_value.tv_sec = s;
	itimer.it_value.tv_nsec = 0;
	itimer.it_interval.tv_sec = 0;
	itimer.it_interval.tv_nsec = 0;
	timerfd_settime(timerFd, 0, &itimer, NULL);
}

void LlcLayer::HandleUserRequest()
{
	struct Data *data = RequestQueueFromUser.front();
	RequestQueueFromUser.pop_front();
	fprintf(stderr, ">> %s\n", data->data);
	int n = write(serialFd, data, sizeof(struct Data)); // TODO manage incomplete write
	if (n < 0) { perror("write error: "); exit(1); }
	delete data;
	StartTimer(3); // 3 seconds
	state = BUSY;
}

void LlcLayer::HandleTimeout()
{
	// timeout
	close(timerFd);
	timerFd = -1;
	fprintf(stderr, "%s: timeout!\n", localName);
	state = READY;
}


void *LlcLayer::MainLoopStatic(void * self)
{
	return ((LlcLayer*)self)->MainLoop();
}
void *LlcLayer::MainLoop()
{
	int nfds = -1;
	fd_set rd, wr;

	state = READY;
	
	while (1) {
		FD_ZERO(&wr);
		FD_ZERO(&rd);
		FD_SET(serialFd, &rd);
		FD_SET(userFd, &rd);
		if (timerFd >= 0) FD_SET(timerFd, &rd);
		nfds = userFd;
		if (serialFd > userFd) nfds = serialFd;
		if ( (timerFd >= 0) && (timerFd > serialFd) ) nfds = timerFd;

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
			if (FD_ISSET(serialFd, &rd)) {
				HandleSerialIndication();
			}

			if (FD_ISSET(userFd, &rd)) {
				HandleUserRequest();
				uint64_t x;
				read(userFd, &x, sizeof(uint64_t));
			}

			if (FD_ISSET(timerFd, &rd)) {
				HandleTimeout();
			}
		}
	}
}



int main(int argc, char **argv)
{
	// usage: test_fsm <device> <name> <remote> <period>
	const char * localName = argv[2];
	LlcLayer fsm;
	fsm.Init(argv[1], localName);
	int fsm_layer = fsm.Connect();
	
	int t = 0;
	int period = atoi(argv[4]);
	while (1) {
		if (t > period*10) {
			// send user data
			struct Data *data = new struct Data;
			memcpy(data->destination, argv[3], 6);
			strcpy(data->data, "ping");
			fsm.DataReq(data);
			t = 0;
		}
		// check if data indication
		struct Data *data;
		fsm.GetIndication(&data);
		if (data) {
			fprintf(stderr, "%s received: %s\n", localName, data->data);
			delete data;
		}
		usleep(100000);
		t++;
		
	}
}
