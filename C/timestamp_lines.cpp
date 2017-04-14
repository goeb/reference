#include <stdio.h>
#include <time.h>
#include <sys/time.h>
#include <string>
#include <iostream>

main()
{
	std::string line;
	struct tm date;
	struct timeval tv;

	while (getline(std::cin, line)) {
		gettimeofday(&tv, 0);
		localtime_r(&tv.tv_sec, &date);
		int milliseconds = tv.tv_usec / 1000;
		printf("%.4d-%.2d-%.2d %.2d:%.2d:%.2d.%03d %s\n", date.tm_year + 1900,
				date.tm_mon + 1, date.tm_mday, date.tm_hour,
				date.tm_min, date.tm_sec, milliseconds,
				line.c_str());
	}
}
