#include <krb5.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


void usage()
{ 
	printf("usage: $0 krb5 <user@REALM> <password>\n");
	exit(1);
}

/* principal = username + "@" + realm
 */

int auth_krb5(char *principal, char *password)
{
    krb5_context ctx;
    memset(&ctx, 0, sizeof(ctx));

    krb5_principal user;
    memset(&user, 0, sizeof(user));

    krb5_error_code code = 0;
    //code = krb5_init_context(&ctx);
    code = krb5_init_secure_context(&ctx);
    if (code) {
        printf("krb5_init_context: %d\n", code);
        return -1;
    }

    code = krb5_parse_name(ctx, principal, &user);
    if (code) {
        printf("krb5_parse_name: %d\n", code);
        krb5_free_context(ctx);
        return -1;
    }
    krb5_creds credentials;
    krb5_get_init_creds_opt *options = 0;
    memset(&credentials, 0, sizeof(credentials));
    code = krb5_get_init_creds_opt_alloc(ctx, &options);
    if (code) {
        printf("krb5_get_init_creds_opt_alloc: %d\n", code);
        krb5_free_principal(ctx, user);
        krb5_free_context(ctx);
        return -1;
    }

    // no need for a long time because no ticket will be used
    krb5_get_init_creds_opt_set_tkt_life(options, 5*60);
    //krb5_get_init_creds_opt_set_renew_life(options, 0);
    krb5_get_init_creds_opt_set_forwardable(options, 0);
    //krb5_get_init_creds_opt_set_proxiable(options, 0);
    krb5_get_init_creds_opt_set_change_password_prompt(options, 0);

    code = krb5_get_init_creds_password(ctx, &credentials, user, password,
                                        0, 0, 0, 0, options);
    int result = -1;
    if (code) {
        if (code == KRB5KDC_ERR_KEY_EXP) {
            // Password has expired
            printf("krb5_get_init_creds_opt_alloc: password expired for '%s'\n", principal);
            result = -2;
        } else {
            printf("Kerberos authentication failed for '%s': %d\n", principal, code);
            result = -1;
        }
    } else {
        // success
        result = 0;
        printf("Kerberos authentication success for '%s'\n", principal);
    }

    krb5_get_init_creds_opt_free(ctx, options);
    krb5_free_principal(ctx, user);
    krb5_free_context(ctx);
    return result;

}

int main(int argc, char **argv)
{
	if (argc < 4) usage();
	if (0 == strcmp("krb5", argv[1])) {
		int r = auth_krb5(argv[2], argv[3]);
		printf("r=%d\n", r);
	} else usage();
}
