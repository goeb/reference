#include <iostream>
#include <fstream>
using namespace std;

main(int argc, char **argv) {
	string filename = argv[1];
	
	fstream f(filename.c_str(), ios_base::in);
	f.seekg(0, ios::end);
	int length = f.tellg();
	f.seekg (0, ios::beg);

	char * buffer;
	buffer = new char [length];
	f.read(buffer, length);
	f.close();
	cout << "-- begin --\n";
	cout << buffer;
	cout << "\n-- end --\n";

}
