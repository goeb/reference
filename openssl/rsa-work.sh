#!/bin/sh

echo openssl genrsa -out mykey.pem 1024
openssl genrsa -out mykey.pem 1024

openssl rsa -pubin -in pubkey.pem -noout -modulus
openssl rsa -pubin -inform PEM -text -noout < pubkey.pem
MODULUS_HEX=$(openssl rsa -pubin -in pubkey.pem -noout -modulus | sed -e "s/Modulus=//")
EXPONENT_DEC=$(openssl rsa -pubin -inform PEM -text -noout -in pubkey.pem | awk '/Exponent/ {print $2}')

print_asn1() {
	cat << EOF
# Start with a SEQUENCE
asn1=SEQUENCE:pubkeyinfo

# pubkeyinfo contains an algorithm identifier and the public key wrapped
# in a BIT STRING
[pubkeyinfo]
algorithm=SEQUENCE:rsa_alg
pubkey=BITWRAP,SEQUENCE:rsapubkey

# algorithm ID for RSA is just an OID and a NULL
[rsa_alg]
algorithm=OID:rsaEncryption
parameter=NULL

# Actual public key: modulus and exponent
[rsapubkey]
n=INTEGER:0x$MODULUS_HEX

e=INTEGER:$EXPONENT_DEC
EOF
}

print_asn1 | openssl asn1parse -genconf /dev/stdin -out pubkey-copy.der

openssl rsa -pubin -in pubkey-copy.der -inform DER -text -pubout -out pubkey-copy.pem -outform PEM -noout

diff pubkey-copy.pem pubkey.pem
