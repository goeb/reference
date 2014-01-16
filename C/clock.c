#include <time.h>

main() {
	
	struct timespec tp;
	int x = clock_gettime(CLOCK_MONOTONIC, &tp);
	printf("tv_sec=%d, tv_nsec=%ld\n", tp.tv_sec, tp.tv_nsec);
}
