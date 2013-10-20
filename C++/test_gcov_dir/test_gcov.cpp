
#include <iostream>
#include <dlfcn.h>

using namespace std;
//#include "ClassA.hpp"
//#include "ClassB.hpp"


int main() {
	void* handle = dlopen("libtest_gcov.so", RTLD_NOW);
	return 0;
	typedef void (*hello_t)();
	hello_t hello = (hello_t) dlsym(handle, "hello");
	const char *dlsym_error = dlerror();
	if (dlsym_error) {
		cerr << "Cannot load symbol 'hello': " << dlsym_error << "\n";
		return 1;
	}
	cout << "Calling hello...\n";
	hello();
	dlclose(handle);

	//A::run();
	
}

