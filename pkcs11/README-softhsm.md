# Setup a Soft HSM for testing

This page shows how to setup a software HSM (pkcs11 provider). It can be useful for testing a program using pkcs11 services.

## Install necessary packages

Install softhsm2:
```
$ sudo apt install softhsm2
```

Install pkcs11-tool:
```
$ sudo apt install opensc
```

Install a openssl pkcs11 engine:
```
$ sudo apt install libengine-pkcs11-openssl
```

## Initialize a token in the pkcs11 provider

Create a configuration for local storage:
```
$ export SOFTHSM2_CONF=softhsm2.conf
$ export TOKENDIR=softhsm2-tokens.d
$ mkdir -p $TOKENDIR

$ cat << EOF > $SOFTHSM2_CONF
# SoftHSM v2 configuration file
directories.tokendir = $TOKENDIR
objectstore.backend = file

# ERROR, WARNING, INFO, DEBUG
log.level = ERROR

# If CKF_REMOVABLE_DEVICE flag should be set
slots.removable = false

# Enable and disable PKCS#11 mechanisms using slots.mechanisms.
slots.mechanisms = ALL

# If the library should reset the state on fork
library.reset_on_fork = false

EOF
```

Initialize a token:
```
$ pkcs11-tool --module /usr/lib/softhsm/libsofthsm2.so --init-token --label token-1 --so-pin 1234
Using slot 0 with a present token (0x0)
Token successfully initialized

$ pkcs11-tool --module /usr/lib/softhsm/libsofthsm2.so --init-pin --label token-1 --so-pin 1234 --pin 0000
Using slot 0 with a present token (0x29217b24)
User PIN successfully initialized
```

## Create a key pair
```
$ pkcs11-tool --module /usr/lib/softhsm/libsofthsm2.so --pin 0000 --keypairgen --token-label "token-1" --label "key-1" --key-type EC:prime256v1
Key pair generated:
Private Key Object; EC
  label:      key-1
  Usage:      decrypt, sign, signRecover, unwrap, derive
  Access:     sensitive, always sensitive, never extractable, local
Public Key Object; EC  EC_POINT 256 bits
  EC_POINT:   044104a42168988997a95cd37957ccb1b55fbd777140d328ff7bf12a02e2efe2103b608d311efdf737166a7e256d91c390311c902c7fbf53d4a6c4a1dd2094ca353be1
  EC_PARAMS:  06082a8648ce3d030107 (OID 1.2.840.10045.3.1.7)
  label:      key-1
  Usage:      encrypt, verify, verifyRecover, wrap, derive
  Access:     local
```

## Import a key pair

Create a key and import it:
```
$ openssl ecparam -name secp256k1 -genkey  | openssl pkcs8 -topk8 -nocrypt -out key-2-priv.pem

$ softhsm2-util --token token-1 --import key-2-priv.pem --label key-2 --id 99 --pin 0000
Found slot 1866682424 with matching token label.
The key pair has been imported.
```

List:
```
$ pkcs11-tool --module /usr/lib/softhsm/libsofthsm2.so --list-objects
Using slot 0 with a present token (0x6f435038)
Public Key Object; EC  EC_POINT 256 bits
  EC_POINT:   044104a42168988997a95cd37957ccb1b55fbd777140d328ff7bf12a02e2efe2103b608d311efdf737166a7e256d91c390311c902c7fbf53d4a6c4a1dd2094ca353be1
  EC_PARAMS:  06082a8648ce3d030107 (OID 1.2.840.10045.3.1.7)
  label:      key-1
  Usage:      encrypt, verify, verifyRecover, wrap, derive
  Access:     local
Public Key Object; EC  EC_POINT 256 bits
  EC_POINT:   0441042b271b839b65db1c6d084886365b910411ff1fab6d96e4f365f420647ef6d058a0dec249467af9e157b0dba53ae9d43a45eba1d798b2c2a360751b5c6ae13349
  EC_PARAMS:  06052b8104000a (OID 1.3.132.0.10)
  label:      key-2
  ID:         99
  Usage:      verify, verifyRecover
  Access:     none
```

Read the public key:
```
$ pkcs11-tool --module /usr/lib/softhsm/libsofthsm2.so --read-object --label key-1 --type pubkey
...
```

## Use openssl for signing and verifying

Sign:
```
$ echo hello | PKCS11_MODULE_PATH=/usr/lib/softhsm/libsofthsm2.so \
               openssl pkeyutl \
                       -engine pkcs11 -keyform engine \
                       -sign -out hello.sig \
                       -inkey "pkcs11:token=token-1;object=key-1;pin-value=0000"
Engine "pkcs11" set.
```

Verify:
```
$ echo hello | PKCS11_MODULE_PATH=/usr/lib/softhsm/libsofthsm2.so \
               openssl pkeyutl \
                       -verify -sigfile hello.sig \
                       -engine pkcs11 -keyform engine \
                       -inkey "pkcs11:token=token-1;object=key-1;pin-value=0000"
Engine "pkcs11" set.
Signature Verified Successfully
```
