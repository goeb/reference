/* linux and solaris */

#include <stdio.h>
#include <sys/time.h>

main ()
{
	struct timeval tv;
	int i=0;

	while (i<10)
	{
		i++;
		gettimeofday (&tv, NULL);
		printf ("tv_sec=%ld, tv_usec=%06ld\n", tv.tv_sec, tv.tv_usec);
		printf ("sleep (1)...\n");
		sleep (1);
	}
}
