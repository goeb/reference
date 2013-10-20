
int computeCrc(unsigned char buffer[4]) {
    int crc = 0;
    int i = 0;
    crc += buffer[i++];
    crc += buffer[i++];
    crc += buffer[i++];
    crc += buffer[i++];
    return crc;
}

# include <stdio.h>

main() {
    int x = computeCrc("1234");
    printf("x=%d\n", x);
}
