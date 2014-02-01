#include <fstream>
#include <iostream>

main()
{
	const char *tmpFilename = "xxx";
	std::ofstream db_file(tmpFilename, std::ios::out | std::ios::trunc);
	db_file << "tutu\n";
	int r = db_file.rdbuf()->pubsync(); // sync to disk
	db_file.close();
	std::cout << "r=" << r << std::endl;
}

