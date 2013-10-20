/* gcc -o formated_date_with_microseconds formated_date_with_microseconds.c -g */
#include <sys/time.h>
#include <unistd.h>

main() {
	char s[100];
	struct timeval tv;

	gettimeofday(&tv, NULL);
	strftime(s, sizeof(s), "%Y/%m/%d-%T", localtime(&(tv.tv_sec)));
	printf("%s.%06d\n", s, tv.tv_usec);
}
