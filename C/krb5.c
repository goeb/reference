       #include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <krb5.h>
#include <com_err.h>

/**
 * gcc krb5.c  -lkrb5 -lcom_err -g -o krb5-sso
 *
 * Usage :
 *     krb5-sso "user name@DOMAIN"
 *
 * DOMAIN must be upper case
 */

#define FAIL(...) do { fprintf(stderr, "FAIL %s:%d ", __FILE__, __LINE__); \
    fprintf(stderr, __VA_ARGS__); fprintf(stderr, "\n"); exit(1); } while (0)

char *progname = "yopyop";

/**
 * @param user
 * Example: toto@example.com
 *          <user>@<realm>
 */
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

    int flags = 0;
    code = krb5_parse_name(ctx, user, &me);
    if (code) {
        com_err(progname, code, "when parsing name %s", user);
        FAIL("krb5_parse_name_flags");
    }

    krb5_creds my_creds;
    krb5_get_init_creds_opt *options = NULL;
    int i;
    memset(&my_creds, 0, sizeof(my_creds));
    code = krb5_get_init_creds_opt_alloc(ctx, &options);
    if (code) {
        com_err(progname, code, "krb5_get_init_creds_opt_alloc");
        FAIL("krb5_get_init_creds_opt_alloc");
    }

    krb5_get_init_creds_opt_set_tkt_life(options, 5*60);
    krb5_get_init_creds_opt_set_renew_life(options, 0);
    krb5_get_init_creds_opt_set_forwardable(options, 0);
    krb5_get_init_creds_opt_set_proxiable(options, 0);


    code = krb5_get_init_creds_password(ctx, &my_creds, me, 0,
                                  krb5_prompter_posix, 0, 0, 0, options);
    if (code) {
        if (code == KRB5KRB_AP_ERR_BAD_INTEGRITY) {
            com_err(progname, 0, "Password incorrect while getting initial ticket");
        } else {
            com_err(progname, code, "getting initial ticket");
        }
        FAIL("krb5_get_init_creds_password");
    } else {
        printf("single sign-on OK\n");
    }

    krb5_get_init_creds_opt_free(ctx, options);
    krb5_free_principal(ctx, me);
}
int main(int argc, char **argv)
{
    login(argv[1], 0);
}
