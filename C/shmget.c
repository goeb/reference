#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
    int read = 1;
    if (argc>=2 && 0==strcmp("-w", argv[1])) {
        read = 0; // write mode
    }
    size_t size = 1024;
    key_t key = 0x1234;
    int shmflg = IPC_CREAT | 0644;
    int shmid = shmget(key, size, shmflg);
    if (shmid == -1) {
        perror("shmget");
        exit(1);
    }
    printf("shmid=%d\n", shmid); 

    void * shbuf = shmat(shmid, NULL, 0);
    if (shbuf == (void*) -1L) {
        perror("shmat");
        exit(1);
    }
    if (read) {
        printf("%s\n", (char *)shbuf);
    } else {
        if (argc>=3) sprintf((char*)shbuf, "%s", argv[2]);
        else sprintf((char*)shbuf, "toto");
    }
}
