

#include <sys/time.h>
#include <stdio.h>
#include <time.h>

main()
{
	struct timespec req;
	struct timespec rem;

	int r = clock_getres(CLOCK_MONOTONIC, &req);
	printf("clock_getres: r=%d, req=%lu.%09lu\n", r, req.tv_sec, req.tv_nsec);

	req.tv_sec = 1;
	req.tv_nsec = 0; // 1 second

	int i = 0;

	struct timeval t0;
	struct timeval t1;
	
	r = gettimeofday(&t1, 0);

	printf("unit: microseconds\n");

	for (i=0; i < 20; i++) {
		// sleep 1 second
		gettimeofday(&t0, 0);
		nanosleep(&req, &rem);

		// check the jitter
		// print delta / t0
		gettimeofday(&t1, 0);
		if (t1.tv_usec >= t0.tv_usec) {
			printf("%06lu\n", t1.tv_usec - t0.tv_usec);
		} else {
			printf("%06lu\n", 1000000 + t1.tv_usec - t0.tv_usec);
		}

	}
}
