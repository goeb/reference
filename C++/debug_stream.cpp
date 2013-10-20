#include <iostream>
#include <ctime>
using namespace std;

class DebugOutputStream 
{
	template <typename T> friend DebugOutputStream& operator << (DebugOutputStream&, const T&);
	friend DebugOutputStream& endl(DebugOutputStream& os);

public:
	DebugOutputStream(ostream& s) : stream(s) { endline=1; }
	// handling for the endl function
	DebugOutputStream& operator<<(DebugOutputStream& (*m)(DebugOutputStream&));

private:
	ostream& stream;
	int endline;
};

DebugOutputStream& DebugOutputStream::operator<<(DebugOutputStream& (*m)(DebugOutputStream&))
{
	return (*m)(*this);
}

DebugOutputStream& endl(DebugOutputStream& out)
{
	out.stream << '\n';
	out.stream.flush();
	out.endline = 1;
	return out;
}

template <typename T> DebugOutputStream& operator << (DebugOutputStream& out, const T& t)
{
	time_t rawtime;
	time(&rawtime);

	if (out.endline) out.stream << "[Debug] [2004-04-18] ";
	out.stream << t;
	out.endline = 0;
	return out;
}
main() {
	DebugOutputStream dcout(cout);
	cout << "Always print me." << "toto="<<12.345<<endl;
	dcout << "ligne 1" << endl;
	dcout << "ligne 2, x=" << 12345 << endl;
	dcout << "ligne 3, y=" << 9.88 << endl;
	dcout << "completed." << endl;
}
