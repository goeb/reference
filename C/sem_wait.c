
#include <stdio.h>
#include <semaphore.h>
#include <string.h>
#include <errno.h>

main()
{
	sem_t sem;

	sem_init(&sem, 0, 0);

	int r = sem_post(&sem);
	printf("sem_post: r=%d", r);
	if (r != 0) printf(", %s", strerror(errno));
	printf("\n");

	r = sem_trywait(&sem);
	printf("sem_trywait: r=%d", r);
	if (r != 0) printf(", %s", strerror(errno));
	printf("\n");

	r = sem_trywait(&sem);
	printf("sem_trywait: r=%d", r);
	if (r != 0) printf(", %s", strerror(errno));
	printf("\n");

}
