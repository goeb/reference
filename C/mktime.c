#include <stdio.h>
#include <time.h>

main(int argc, char **argv) {

	struct tm t_tm;
	t_tm.tm_wday = 0;
	t_tm.tm_yday = 0;
	t_tm.tm_sec = t_tm.tm_min = t_tm.tm_hour = 0;
	t_tm.tm_mday = 23;
	t_tm.tm_mon = 4;
	t_tm.tm_year = atoi(argv[1])-1900;
	time_t t = mktime(&t_tm);
	printf("t=%d\n", t);


}
