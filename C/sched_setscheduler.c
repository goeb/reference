       #define _GNU_SOURCE         /* See feature_test_macros(7) */
       #include <unistd.h>
       #include <sys/syscall.h>   /* For SYS_xxx definitions */
#include <sched.h>
#include <string.h>
#include <errno.h>
#include <stdio.h>


int fred_setprio(int priority, int cpu)
{
        int rc;
        int err = 0;
        unsigned long tid = (unsigned long)syscall(SYS_gettid);

        if(cpu>=0) {
                cpu_set_t csmask;

                CPU_ZERO(&csmask);
                CPU_SET(cpu, &csmask);
                rc = sched_setaffinity(tid, sizeof(cpu_set_t), &csmask);
                if(rc<0) {
                        printf("sched_setaffinity(tid=%lu): %s\n",
                                tid, strerror(errno));
                        err = -1;
                }
                if(1) printf("tbox_setprio(tid=%lu) : setaffinity ok\n", tid);
        }

        if(priority>0) {
                struct sched_param sp;
                memset(&sp, 0x00, sizeof(sp));
                sp.sched_priority = priority;
                rc = sched_setscheduler(tid, SCHED_FIFO, &sp);
                if(rc) {
                        printf("sched_setscheduler(tid=%lu): %s\n",
                                tid, strerror(errno));
                        err = -1;
                }
                if(1) printf("tbox_setprio(tid=%lu) : setscheduler ok\n", tid);
        }
        return err;
}

int main() {}
