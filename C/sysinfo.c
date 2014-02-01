#include <sys/sysinfo.h>
#include <stdio.h>
main()
{
	struct sysinfo info;
	int x = sysinfo(&info);
	printf("x=%d, loads=[%ld, %ld, %ld]\n", x, info.loads[0], info.loads[1], info.loads[2]);
}
