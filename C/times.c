/* only for solaris */

#include <stdio.h>
#include <sys/times.h>
#include <limits.h>
#include <string.h>
#include <errno.h>

main ()
{
	struct tms buffer;
	clock_t clock; /* type is long (time.h) */
	int i=0;

	printf ("CLK_TCK=%d\n", CLK_TCK);
	while (i<10)
	{
		i++;
		clock = times (&buffer);
		if (clock == (clock_t)-1)
		{
			fprintf (stderr, "times error : %s\n", strerror (errno));
			exit (1);
		}
		printf ("clock=%ld\n", clock);
		printf ("sleep (1)...\n");
		sleep (1);
	}
}
