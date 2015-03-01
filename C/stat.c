
 #include <stdio.h>
       #include <sys/types.h>
       #include <sys/stat.h>
       #include <unistd.h>
int main (int argc, char **argv) 
{
    struct stat fileStat;
    int r = stat(argv[1], &fileStat);
    printf("path: %s\n", argv[1]);
    printf("r: %d\n", r);
    if (r==0) {
        printf("S_ISREG: %d\n", S_ISREG(fileStat.st_mode));
        printf("S_ISDIR: %d\n", S_ISDIR(fileStat.st_mode));
        printf("S_ISCHR: %d\n", S_ISCHR(fileStat.st_mode));
        printf("S_ISBLK: %d\n", S_ISBLK(fileStat.st_mode));
        printf("S_ISFIFO: %d\n", S_ISFIFO(fileStat.st_mode));
        printf("S_ISLNK: %d\n", S_ISLNK(fileStat.st_mode));
        printf("S_ISSOCK: %d\n", S_ISSOCK(fileStat.st_mode));
    }
}
