#include <openssl/bio.h>
#include <stdio.h>
#include <string>

std::string get_bio_mem_string(BIO *buffer)
{
    char *ptr;
    long datalen = BIO_get_mem_data(buffer, &ptr);
    if (datalen < 0 || !ptr) {
        fprintf(stderr, "BIO_get_mem_data error");
        return "";
    }
    return std::string(ptr, datalen);
}

