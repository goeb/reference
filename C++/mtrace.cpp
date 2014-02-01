// experiment mtrace leak detector

#include <stdlib.h>

#ifdef MTRACE
	#include <mcheck.h>
#endif
#include <list>

//#include "dmalloc.h"

class AAA {
	int x;
	char y[123];
};

int main()
{
	#ifdef MTRACE
        mtrace(); /* Starts the recording of memory allocations and releases */
	#endif
 
        void* a = NULL;
 
        a = malloc(sizeof(int)); /* allocate memory and assign it to the pointer */
        a = malloc(sizeof(int)); /* allocate memory and assign it to the pointer */
        if (a == NULL) {
                return 1; /* error */
        }

		std::list<int> L;
		L.push_back(123);
		L.push_back(456);
	
		AAA *y = new AAA;
		AAA *y2 = new AAA;

 
        //free(a); /* we free the memory we allocated so we don't have leaks */
	#ifdef MTRACE
        muntrace();
	#endif
 
	//dmalloc_shutdown();
        return 0; /* exit */
}
