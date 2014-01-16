#include <stdio.h>
#include <time.h>

#include <sys/time.h>

main()
{
	struct tm date;
	struct timeval tv;
	gettimeofday(&tv, 0);
	localtime_r(&tv.tv_sec, &date);
	int milliseconds = tv.tv_usec / 1000;
	printf("%.4d-%.2d-%.2d %.2d:%.2d:%.2d.%03d\n", date.tm_year + 1900,
			date.tm_mon + 1, date.tm_mday, date.tm_hour,
			date.tm_min, date.tm_sec, milliseconds);
}
