#include <stdio.h>
#include <stdio.h>
#include <readline/readline.h>
#include <readline/history.h>
#include <stdlib.h>
#include <sasl.h>
#include <ldap.h>

void usage()
{
	printf("usage: ldapClient <server> <DN> <mechanism>\n");
	printf("\n");
	printf("Example:");
	printf("    ldapClient ldap://example.com:389 \"uid=John Doo,ou=people,dc=example,dc=com\" GSSAPI\n");
	exit(1);
}
typedef struct {
    char* username;
    char* password;
} my_authdata;

int my_sasl_interact(LDAP *ld, unsigned flags, void *defaults, void *in)
{
    my_authdata *auth=(my_authdata*)defaults;

    sasl_interact_t *interact = (sasl_interact_t*)in;
    if( ld == NULL ) return LDAP_PARAM_ERROR;

    while( interact->id != SASL_CB_LIST_END ) {

        char *dflt = (char*)interact->defresult;

        switch( interact->id ) {
            case SASL_CB_GETREALM:
                dflt=NULL;
                break;
            case SASL_CB_AUTHNAME:
                dflt=auth->username;
                break;
            case SASL_CB_PASS:
                dflt=auth->password;
                break;
            default:
                printf("my_sasl_interact asked for unknown %i\n",interact->id);
        }
        interact->result = (dflt && *dflt) ? dflt : (char*)"";
        interact->len = strlen( (char*)interact->result );

        interact++;
    }
    return LDAP_SUCCESS;
}

int main(int argc, char **argv)
{
    LDAP        *ld = NULL;

    int        rc;

    /* Get username and password */
    if (argc != 4) {
		usage();
    }
	const char *password = 0;
    // read password
    password = readline("Password: ");
    printf("password='%s'\n", password);

    static my_authdata auth;
    auth.username = argv[2];
    auth.password = password;

    int authmethod = LDAP_AUTH_SASL;
    char *sasl_mech = strdup(argv[3]); // eg: "DIGEST-MD5"
    char *ldapuri = strdup(argv[1]);

    int protocol = LDAP_VERSION3;
    unsigned sasl_flags = LDAP_SASL_QUIET;
    char *binddn=NULL;

    /* Open LDAP Connection */
    rc = ldap_initialize( &ld, ldapuri );
    if (rc != LDAP_SUCCESS ) {
        fprintf( stderr, "Could not create LDAP session handle (%d): %s\n", rc, ldap_err2string(rc) );
        return 1;
    }

    if( ldap_set_option( ld, LDAP_OPT_PROTOCOL_VERSION, &protocol ) != LDAP_OPT_SUCCESS ) {
        fprintf( stderr, "Could not set LDAP_OPT_PROTOCOL_VERSION %d\n", protocol );
        return 1;
    }  

    rc = ldap_sasl_interactive_bind_s( ld, binddn,
                  sasl_mech, NULL, NULL,
                  sasl_flags, my_sasl_interact, &auth );

    if( rc != LDAP_SUCCESS ) {
        ldap_perror( ld, "ldap_sasl_interactive_bind_s" );
        ldap_unbind_ext_s( ld,NULL,NULL);
        return 1;
    }
    printf("Successful authentication\n");
    rc=ldap_unbind_ext_s( ld,NULL,NULL);
    sasl_done();
    sasl_client_init( NULL );
    return 0;
}
