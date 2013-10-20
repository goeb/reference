#include <stdio.h>
#include <dlfcn.h>
#include <stdlib.h>

#include "Wagon.hpp"

int main(int argc, char **argv) {

    cout << "Starting...\n";
    void *handle;
    typedef int(*func)(int);
    int (*square)(int);
    const char *error;
    handle = dlopen ("./libshared.so", RTLD_NOW | RTLD_GLOBAL);
    if (!handle) {
        fputs (dlerror(), stderr);
        exit(1);
    }

    square = (int (*)(int))dlsym(handle, "square");
    if ((error = dlerror()) != NULL)  {
        fputs(error, stderr);
        exit(1);
    }

    printf ("%d\n", (*square)(1));
    printf ("%d\n", (*square)(2));
    printf ("%d\n", (*square)(3));

    Wagon* (*wagon_factory)(string &);
    wagon_factory = (Wagon* (*)(string &))dlsym(handle, "createWagon");
    string wagonName("toto");
    Wagon* wagon1 = wagon_factory(wagonName);
    wagon1->print();

    dlclose(handle);
    cout << "after dlclose()\n";

    delete wagon1;
    cout << "after delete wagon1\n";
}

