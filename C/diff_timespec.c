#include <stdio.h>
#include <time.h>
#include <unistd.h>

int diff_elapsed_time(const struct timespec *initial_time, int timeout_ms)
{
	struct timespec current_time;
	int diff_timeout_ms;
	int err = clock_gettime(CLOCK_MONOTONIC, &current_time);
	if (err) {
		perror("progress_ipc_recv_ack: clock_gettime");
		return -1;
	}
	struct timespec elapsed;
	elapsed.tv_sec = current_time.tv_sec - initial_time->tv_sec;
	elapsed.tv_nsec = current_time.tv_nsec - initial_time->tv_nsec;

	diff_timeout_ms = timeout_ms - (elapsed.tv_sec*1000 + elapsed.tv_nsec/1E6);

	return diff_timeout_ms;
}

int main()
{
	struct timespec initial_time;
	int timeout_ms = 3000;
	int err = clock_gettime(CLOCK_MONOTONIC, &initial_time);
	if (err) {
		perror("clock_gettime");
		return 1;
	}
	printf("diff_elapsed_time: %d\n", diff_elapsed_time(&initial_time, timeout_ms));
	usleep(500000);
	printf("diff_elapsed_time: %d\n", diff_elapsed_time(&initial_time, timeout_ms));
	usleep(500000);
	printf("diff_elapsed_time: %d\n", diff_elapsed_time(&initial_time, timeout_ms));
	usleep(500000);
	printf("diff_elapsed_time: %d\n", diff_elapsed_time(&initial_time, timeout_ms));
	usleep(500000);
	printf("diff_elapsed_time: %d\n", diff_elapsed_time(&initial_time, timeout_ms));
	usleep(500000);
	printf("diff_elapsed_time: %d\n", diff_elapsed_time(&initial_time, timeout_ms));
	usleep(500000);
	printf("diff_elapsed_time: %d\n", diff_elapsed_time(&initial_time, timeout_ms));
}
