
#include <stdio.h>
#include <fstream>

main(int argc, char **argv)
{
    const int LINE_SIZE_MAX = 20;
    char line[LINE_SIZE_MAX];
	std::ifstream ifs(argv[1], std::ifstream::in);

	if (!ifs.good()) { printf("error\n"); return 1; }

	while (ifs.getline(line, LINE_SIZE_MAX)) {
		printf("line: %s\n", line);
	}	
	if (ifs.eof()) printf("ok\n");
	else printf("error: line too long or other\n");
}
