#include <stdlib.h>
#include <string.h>
#include <vector>
#include <stdio.h>
#include <unistd.h>

// usage:
//     CharStarVectorWrapper argv;
//     argv.add("pppd");
//     argv.add("nodetach");
//     argv.add("defaultroute");
//     execvp("pppd", argv.GetVector());
class CharStarVectorWrapper
{
public:
	inline void add(const char *s) {
		char *s2 = const_cast<char *>(s);
		v.push_back(s2);
	}
	char ** GetVector() { return &v[0]; }

//	~CharStarVectorWrapper() {
//		std::vector<char*>::iterator i;
//		for (i = v.begin(); i != v.end(); i++) {
//			free(*i);
//		}
//	}
private:
	std::vector<char*> v;

};


// int execvp(const char *file, char *const argv[]);

main()
{
	CharStarVectorWrapper argv;
	argv.add("ls");
	argv.add("xxx");
	argv.add("yyy");
	execvp("ls", argv.GetVector());
}
