
/*
 * i686-w64-mingw32-gcc  LockFileEx.c
 */
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

#define NUMWRITES 10
#define TESTSTRLEN 11

const char TestData[NUMWRITES][TESTSTRLEN] = 
{ 
    "TestData0\n",
    "TestData1\n",
    "TestData2\n",
    "TestData3\n",
    "TestData4\n",
    "TestData5\n",
    "TestData6\n",
    "TestData7\n",
    "TestData8\n",
    "TestData9\n"
};

int main(int argc, char *argv[])
{
    BOOL fSuccess = FALSE;

    // Create the file, open for both read and write.
    HANDLE hFile = CreateFile(TEXT("datafile.txt"),
                       GENERIC_READ | GENERIC_WRITE,
                       0,          // open with exclusive access
                       NULL,       // no security attributes
                       CREATE_NEW, // creating a new temp file
                       0,          // not overlapped index/O
                       NULL);
    
    if (hFile == INVALID_HANDLE_VALUE) 
    {
        // Handle the error.
        printf("CreateFile failed (%d)\n", GetLastError());
        return (1);
    }

    // Lock the 4th write-section.  
    // First, set up the Overlapped structure with the file offset 
    // required by LockFileEx, three lines in to the file.
    OVERLAPPED sOverlapped;
    sOverlapped.Offset = TESTSTRLEN * 3;
    sOverlapped.OffsetHigh = 0;

    // Actually lock the file.  Specify exclusive access, and fail 
    // immediately if the lock cannot be obtained.
    fSuccess = LockFileEx(hFile,         // exclusive access, 
                          LOCKFILE_EXCLUSIVE_LOCK | 
                          LOCKFILE_FAIL_IMMEDIATELY,
                          0,             // reserved, must be zero
                          0,    // number of bytes to lock
                          0,
                          &sOverlapped); // contains the file offset
    if (!fSuccess) 
    {
       // Handle the error.
       printf ("LockFileEx failed (%d)\n", GetLastError());
       return (3);
    }
    else printf("LockFileEx succeeded\n");

    sleep(10);
    /////////////////////////////////////////////////////////////////
    // Add code that does something interesting to locked section,  /
    // which should be line 4                                       /
    /////////////////////////////////////////////////////////////////

    // Unlock the file.
    fSuccess = UnlockFileEx(hFile, 
                            0,             // reserved, must be zero
                            TESTSTRLEN,    // num. of bytes to unlock
                            0,
                            &sOverlapped); // contains the file offset
    if (!fSuccess) 
    {
       // Handle the error.
       printf ("UnlockFileEx failed (%d)\n", GetLastError());
       return (4);
    }
    else printf("UnlockFileEx succeeded\n");

    // Clean up handles, memory, and the created file.
    fSuccess = CloseHandle(hFile);
    if (!fSuccess) 
    {
       // Handle the error.
       printf ("CloseHandle failed (%d)\n", GetLastError());
       return (5);
    }

    fSuccess = DeleteFile(TEXT("datafile.txt"));
    if (!fSuccess) 
    {
        // Handle the error.
       printf ("DeleteFile failed (%d)\n", GetLastError());
       return (6);
    }
    return (0);
}
