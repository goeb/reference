#include <stdio.h>
#include <ldap.h>

void usage()
{
	printf("usage: ldapClient <server> <CN> <password>\n");
	printf("\n");
	printf("Example:");
	printf("    ldapClient ldap://example.com:389 \"John Doo\" abcdef\n");
}

int main(int argc, char **argv)
{
    LDAP        *ld;
    int        rc;
    char        bind_dn[100];

    /* Get username and password */
    if( argc != 4 )
    {
        perror( "invalid args, required: <server> <CN> <password>" );
		usage();
        return( 1 );
    }
    const char *server = argv[1]; // ex: "ldap://nafiux.com:389"
    const char *cn = argv[2]; // common name
    const char *password = argv[3];
    printf( "Connecting as %s...\n", cn );

    /* Open LDAP Connection */
    if( ldap_initialize( &ld, server ) )
    {
        perror( "ldap_initialize" );
        return( 1 );
    }

    /* User authentication (bind) */
    rc = ldap_simple_bind_s( ld, cn, password);
    if( rc != LDAP_SUCCESS )
    {
        fprintf(stderr, "ldap_simple_bind_s: %s\n", ldap_err2string(rc) );
        return( 1 );
    }
    printf( "Successful authentication\n" );
    ldap_unbind( ld );
    return( 0 );
}
