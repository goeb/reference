
#include <sys/sysinfo.h>

main()
{
	struct sysinfo info;
	sysinfo(&info);
	printf("Uptime = %d\n",info.uptime);
}
