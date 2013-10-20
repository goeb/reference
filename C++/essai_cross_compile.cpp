
/*
 * i586-mingw32msvc-g++ -o essai_cross_compile.exe essai_cross_compile.cpp
 */
    #include <windows.h>  
      
    int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,  
        LPSTR lpCmdLine, int nCmdShow)  
    {  
      MessageBox(NULL,  
        "Cette fenêtre prouve que le cross-compilateur est fonctionnel !",  
        "Hello World", MB_OK);  
      return 0;  
    }  
