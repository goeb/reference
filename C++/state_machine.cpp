#include <iostream>
#include <vector>
using namespace std;

enum SigId {
	PING,
	PONG
};

class Process {
public:
	char *name;
	Process(char *n) {
		name = n;
	}
};

class Signal {
public:
	enum SigId id;
	Signal() { }
	Signal(enum SigId id_) : id(id_) { }
	Process *sender;
	Process *destination;
};

class Ping : public Signal {
public:
	Ping() : Signal(PING) { }
	string message;
	int i;
};
class Pong : public Signal {
public:
	Pong() : Signal(PONG) { }
	string message;
	int i;
};

vector<Signal *> signal_stack;


void output(Process *destination, Signal *s) {
	s->destination = destination;
	signal_stack.push_back(s);
}

class Process1 : public Process {
public:
	int state;
	int counter;
	Process1(char *name) : Process(name) { state = 0; counter = 0;}
	void input(Signal *s) {
		cout << name << ": received signal " << s->id << "\n";
		if (state == 0) {
			cout << name << ": state 0 -> 1\n";
			state = 1;
		} else {
			cout << name << ": state 1 -> 0\n";
			state = 0;
		}
		counter++;
		Pong *p = new Pong();
		output(s->sender, p);
	}
};

class Process2 : public Process {
public:
	void start() {
		
	}
	int counter;
	Process2(char *name) : Process(name) { counter = 0;}
	void input(Signal *s) {
		cout << name << ": received signal " << s->id << " (" << counter << ")\n";
		counter++;
		delete s;
	}
};

main() {
	Process1 p1("first");
	Process2 p2("second");
	
}
