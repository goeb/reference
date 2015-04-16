#include <stdio.h>
#include <stdio.h>
#include <readline/readline.h>
#include <readline/history.h>
#include <stdlib.h>
#include <ldap.h>

void usage()
{
	printf("usage: ldapClient <server> <DN> <mechanism>\n");
	printf("\n");
	printf("Example:");
	printf("    ldapClient ldap://example.com:389 \"uid=John Doo,ou=people,dc=example,dc=com\" GSSAPI\n");
	exit(1);
}

int main(int argc, char **argv)
{
    LDAP        *ld;
    int        rc;

    /* Get username and password */
    if (argc != 4) {
		usage();
    }
	const char *password = 0;
    // read password
    password = readline("Password: ");
    printf("password='%s'\n", password);

    const char *mechanism = argv[3];
    const char *server = argv[1];
    const char *dn = argv[2];
    printf ("Connecting as %s...\n", dn);

    /* Open LDAP Connection */
    if (ldap_initialize(&ld, server))
    {
        perror("ldap_initialize");
        return 1;
    }

	int version = LDAP_VERSION3;
	ldap_set_option(ld, LDAP_OPT_PROTOCOL_VERSION, &version);

    /* User authentication (bind) */
    struct berval cred;
    cred.bv_len = strlen(password); // remove the 'const'
    cred.bv_val = strdup(password);

	struct berval *servcred;
	//LDAPControl clientctrls[2];
	//clientctrls[0].ldctl_oid = 

    rc = ldap_sasl_bind_s(ld, dn, mechanism, &cred, 0, 0, &servcred);
    if (rc != LDAP_SUCCESS) {
        fprintf(stderr, "ldap_simple_bind_s: %s\n", ldap_err2string(rc) );
        return( 1 );
    }
    printf("Successful authentication\n");
    ldap_unbind_ext(ld, 0, 0);
    return 0;
}
