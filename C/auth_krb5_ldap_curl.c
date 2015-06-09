
/*
     gcc -Wall auth_krb5_ldap_curl.c \
		-I/usr/include/mit-krb5 -L/usr/lib/i386-linux-gnu/mit-krb5 -lkrb5 \
		-lldap \
		-I /usr/include/curl -lcurl

 *
 */
#include <krb5.h>
#include <ldap.h>
#include <curl/curl.h>


#include <stdlib.h>
#include <stdio.h>
#include <string.h>


void usage()
{ 
	printf("usage: $0 krb5 <user@REALM> <password>\n");
	printf("       $0 ldap <uri> <dname> <password>\n");
	printf("       $0 curl <url>\n");
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


int auth_ldap(char *uri, char *dname, char *password)
{
	LDAP *ld;
    int result;

    // Open LDAP Connection
    int r = ldap_initialize(&ld, uri);
    if (r != LDAP_SUCCESS) {
        printf("ldap_initialize error for server '%s': %s\n", uri, ldap_err2string(r));
        return -1;
    }
    int version = LDAP_VERSION3;
    r = ldap_set_option(ld, LDAP_OPT_PROTOCOL_VERSION, &version);
    if (r != LDAP_SUCCESS) {
        printf("ldap_set_option error for server '%s': %s\n", uri, ldap_err2string(r));
        ldap_unbind_ext(ld, 0, 0);
        result = -1;
    }

    struct berval cred;
    cred.bv_len = strlen(password);
    cred.bv_val = password;

    struct berval *servcred = 0;

    // User authentication
    r = ldap_sasl_bind_s(ld, dname, 0, &cred, 0, 0, &servcred);
    if (r != LDAP_SUCCESS) {
        printf("ldap_simple_bind_s error for '%s': %s\n", dname, ldap_err2string(r));
        result = -1;
    } else {
        printf("Ldap authentication success for user '%s'\n", dname);
        result = 0;
    }
    if (servcred) {
        // free server credentials TODO
    }

    r = ldap_unbind_ext(ld, 0, 0);
    if (r != LDAP_SUCCESS) {
        printf("ldap_unbind error for user '%s': %s",  dname, ldap_err2string(r));
    }

    return result;

}

int curl_get(char *url)
{
	CURL *curl;
	CURLcode res;

	curl = curl_easy_init();
	if (curl) {
		curl_easy_setopt(curl, CURLOPT_URL, "url");
		/* example.com is redirected, so we tell libcurl to follow redirection */ 
		curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);

		/* Perform the request, res will get the return code */ 
		res = curl_easy_perform(curl);
		/* Check for errors */ 
		if (res != CURLE_OK)
			printf("curl_easy_perform() failed: %s\n", curl_easy_strerror(res));

		/* always cleanup */ 
		curl_easy_cleanup(curl);
	}
	return 0;
}

int main(int argc, char **argv)
{
	if (argc < 3) usage();
	if (0 == strcmp("krb5", argv[1])) {
		if (argc < 4) usage();
		int r = auth_krb5(argv[2], argv[3]);
		printf("auth_krb5: r=%d\n", r);

	} else if (0 == strcmp("curl", argv[1])) {
		int r = curl_get(argv[2]);
		printf("curl_get: r=%d\n", r);

	} else if (0 == strcmp("ldap", argv[1])) {
		if (argc < 5) usage();
		int r = auth_ldap(argv[2], argv[3], argv[4]);
		printf("auth_ldap: r=%d\n", r);

	} else usage();

	return 0;
}
