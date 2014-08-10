#include <stdio.h>
#include <ldap.h>

int main(int argc, char **argv)
{
    LDAP        *ld;
    int        rc;
    char        bind_dn[100];

    /* Get username and password */
    if( argc != 4 )
    {
        perror( "invalid args, required: server who password" );
        return( 1 );
    }
    const char *server = argv[1]; // ex: "ldap://nafiux.com:389"
    const char *who = argv[2]; // ex: cn=toto,ou=People,dc=nafiux,dc=com
    const char *password = argv[3];
    printf( "Connecting as %s...\n", who );

    /* Open LDAP Connection */
    if( ldap_initialize( &ld, server ) )
    {
        perror( "ldap_initialize" );
        return( 1 );
    }

    /* User authentication (bind) */
    rc = ldap_simple_bind_s( ld, who, password);
    if( rc != LDAP_SUCCESS )
    {
        fprintf(stderr, "ldap_simple_bind_s: %s\n", ldap_err2string(rc) );
        return( 1 );
    }
    printf( "Successful authentication\n" );
    ldap_unbind( ld );
    return( 0 );
}
