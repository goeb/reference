#include <sys/statvfs.h>
#include <stdio.h>

main()
{
	struct statvfs stat;
	int result = statvfs("/", &stat); // check NOR (rootfs)
	printf("statvfs(/)=%d, f_bavail=%lu, f_blocks=%lu\n", result, stat.f_bavail, stat.f_blocks);
	float ratio = 1.0*stat.f_bavail/stat.f_blocks;
	int usagePercent = 100-100*ratio;
	printf("ratio=%f, usagePercent=%d\n", ratio, usagePercent);
}
