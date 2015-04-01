#include <k5-int.h>
#include "k5-platform.h"        /* for asprintf */
#include <krb5.h>
#include <com_err.h>

/**
 * gcc krb5.c -I ~/Downloads/krb5-1.13.1/src/include -lkrb5 -g
 */

#define FAIL(...) do { fprintf(stderr, "FAIL %s:%d ", __FILE__, __LINE__); \
    fprintf(stderr, __VA_ARGS__); fprintf(stderr, "\n"); exit(1); } while (0)

char *progname = "yopyop";

void login(const char *user, const char *password)
{

    krb5_context ctx;
    krb5_principal me;
    memset(&ctx, 0, sizeof(ctx));
    memset(&me, 0, sizeof(me));
    krb5_error_code code = 0;
//  k5_begin
    code = krb5_init_context(&ctx);
    if (code) {
        com_err(progname, code, "while initializing Kerberos 5 library");
        FAIL("krb5_init_context");
    }
    me = user;
    
// k5_kinit 

    struct k_opts* opts;
    krb5_creds my_creds;
    krb5_get_init_creds_opt *options = NULL;
    int i;
    memset(&my_creds, 0, sizeof(my_creds));
    code = krb5_get_init_creds_opt_alloc(ctx, &options);
    if (code) {
        com_err(progname, code, "krb5_get_init_creds_opt_alloc");
        FAIL("krb5_get_init_creds_opt_alloc");
    }

    code = krb5_get_init_creds_password(ctx, &my_creds, me,
                                            0, krb5_prompter_posix, 0, 0, 0, 0);
    if (code) {
        com_err(progname, code, "krb5_get_init_creds_opt_alloc");
        FAIL("krb5_get_init_creds_password");
    }


}
int main(int argc, char **argv)
{
    login(argv[1], 0);
}
