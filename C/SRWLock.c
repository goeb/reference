
/*
 * i686-w64-mingw32-gcc SRWLock.cpp -D_WIN32_WINNT=0x0600
 */

#include <windows.h>
#include <synchapi.h>
#include <stdio.h>
SRWLOCK L;

DWORD WINAPI myThread(LPVOID lpParameter)
{
	printf("AcquireSRWLockExclusive\n");
    AcquireSRWLockExclusive(&L);
    // do something
	printf("ReleaseSRWLockExclusive\n");
    ReleaseSRWLockExclusive(&L);
}

int main()
{
    int i;

    InitializeSRWLock(&L);

	unsigned int myCounter = 0;
    for(i=0;i<3;i++) {
		DWORD myThreadID;
		HANDLE myHandle = CreateThread(0, 0, myThread, &myCounter, 0, &myThreadID);

	}
}

