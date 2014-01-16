#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sstream>

void print_open_fd()
{
	pid_t pid = getpid();
	std::ostringstream cmd;
	cmd << "ls -l /proc/" << pid << "/fd";
	system(cmd.str().c_str());
}

const char * test_filename = "/tmp/test_fstream_close.x";

void test_ifstream_close() 
{
	std::ifstream db_file(test_filename);
	std::cout << "test_ifstream_close" << std::endl;	
	print_open_fd();
}
void test_ofstream_close() 
{
	std::ofstream db_file(test_filename);
	std::cout << "test_ofstream_close" << std::endl;	
	print_open_fd();
}

main()
{
    std::ifstream db_file("tmp.x");
    int x=0, y=0, z=0;
    db_file >> x;
    char c = 0;
    db_file.get(c); 
    db_file >> y;
    db_file.get(c);
    db_file >> z;
    printf("x=%d, y=%d, z=%d\n", x, y, z);

	test_ofstream_close();
	std::cout << "test_ofstream finished" << std::endl;
	print_open_fd();
	test_ifstream_close();
	std::cout << "test_ifstream finished" << std::endl;
	print_open_fd();
}
