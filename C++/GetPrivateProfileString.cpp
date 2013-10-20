
/*
 * i586-mingw32msvc-g++  GetPrivateProfileString.cpp -o GetPrivateProfileString.exe
 */



#include <windows.h> 
#include <tchar.h>
#include <stdio.h> 
#include <iostream>
using namespace std;
 
int main() 
{ 
    cout << "starting..." << endl;
    const int N = 1000;
   TCHAR   inBuf[N]; 
 
   // Test 
   GetPrivateProfileString (TEXT("Section1"), 
                            TEXT("FirstKey"), 
                            TEXT("Error: GPPS failed"), 
                            inBuf, 
                            N, 
                            TEXT("./appname.ini")); 

    cout << "GetPrivateProfileString done" << endl;
    
   cout << "Key: " << inBuf << endl; 

   GetPrivateProfileSection ("Section2", 
                            inBuf, 
                            N, 
                            "./appname.ini"); 
 
   char *p = inBuf;
   while (p && *p)
   {
        cout << "Section1: " << p << endl;
        p += strlen(p) + 1;
   }
   return 0;
}


