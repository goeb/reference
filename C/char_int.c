


    #include "stdio.h"
    int main(){
           int a=1;
           printf("%c",*(((char *)&a)+1)+65);
           printf("%c",*(((char *)&a)+2)+65);
           printf("%c",*(((char *)&a)+3)+65);
    } 
