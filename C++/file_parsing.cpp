#include <iostream>
#include <fstream>


using namespace std;

main() 
{
	std::ifstream file;
	unsigned long long L_userCpuTime=0, unused=0, L_sysCpuTime=0, L_idleCpuTime = 0;
	file.open("/proc/stat", std::ios_base::in);
	file.ignore(256, '\n').ignore(10, ' ');
    file >> L_userCpuTime;
    file >> unused;
    file >> L_sysCpuTime;
    file >> L_idleCpuTime;

	cout << "L_userCpuTime=" << L_userCpuTime << 
		    ", unused=" << unused << 
		    ", L_sysCpuTime=" << L_sysCpuTime 	<<
		    ", L_idleCpuTime=" << L_idleCpuTime <<	
			endl;

}
