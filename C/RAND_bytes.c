#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <stdio.h>
#include <openssl/rand.h>
#include <openssl/err.h>

void dump(unsigned char *buf, int len, const char *label)
{
    size_t i;
    if (label) printf("%s: ", label);

    for (i=0; i<len; i++) {
        printf("%02x", buf[i]);
    }
    printf("\n");
}
int main(int argc, char **argv)
{
    int N = 100;
    if (argc >= 2) N = atoi(argv[1]);

    unsigned char *buf = (unsigned char *)malloc(N);
    if (!buf) {
        printf("malloc error: %s\n", strerror(errno));
        exit(1);
    }
    int r = RAND_bytes(buf, N);
    if (r != 1) {
        printf("RAND_bytes error: %s\n", ERR_error_string(ERR_get_error(), NULL));
    } else {
        dump(buf, N, "RAND_bytes       ");
    }

    r = RAND_pseudo_bytes(buf, N);
    if (r != 1) {
        printf("RAND_pseudo_bytes error: %s\n", ERR_error_string(ERR_get_error(), NULL));
    } else {
        dump(buf, N, "RAND_pseudo_bytes");
    }
}
