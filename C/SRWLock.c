
/*
 * i686-w64-mingw32-gcc SRWLock.cpp -D_WIN32_WINNT=0x0600
 */

#include <windows.h>
#include <synchapi.h>
#include <stdio.h>

SRWLOCK L;
unsigned int Counter;

DWORD WINAPI worker_writer(LPVOID lpParameter)
{
    int i = 0;
    for (i=0;i<100;i++) {
        AcquireSRWLockExclusive(&L);
        Counter++;
	    printf("writer: counter=%u\n", Counter);
        ReleaseSRWLockExclusive(&L);
    }
}
DWORD WINAPI worker_reader(LPVOID lpParameter)
{
    int i = 0;
    for (i=0;i<100;i++) {
        AcquireSRWLockShared(&L);
        // do something
	    printf("reader: counter=%u\n", Counter);
        ReleaseSRWLockShared(&L);
    }
}

int main()
{
    int i;

    InitializeSRWLock(&L);

	unsigned int myCounter = 0; // not used
    // launch 100 readers
    for (i=0;i<100;i++) {
		DWORD myThreadID;
		HANDLE myHandle = CreateThread(0, 0, worker_reader, &myCounter, 0, &myThreadID);
	}
    // launch 100 writers writers
    for (i=0;i<100;i++) {
		DWORD myThreadID;
		HANDLE myHandle = CreateThread(0, 0, worker_writer, &myCounter, 0, &myThreadID);
	}

}

