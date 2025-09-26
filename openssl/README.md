# Openssl

## Sign and Verify

### RSA

- Generate a key pair
```
openssl genrsa -out key-rsa4096-priv.pem 4096
openssl rsa -in key-rsa4096-priv.pem -pubout > key-rsa4096-pub.pem
```

- Sign `"hello\n"`
```
echo hello | openssl pkeyutl -sign \
                             -inkey key-rsa4096-priv.pem \
                             -rawin -digest sha256 \
           > hello-rsa4096.sig
```

- Verify `"hello\n"`
```
echo hello | openssl pkeyutl -verify \
                             -inkey key-rsa4096-pub.pem -pubin \
                             -sigfile hello-rsa4096.sig \
                             -rawin -digest sha256
Signature Verified Successfully
```

### ECC

- Generate a key pair
```
openssl ecparam -name prime256v1 -genkey -out key-ec-prime256v1-priv.pem
openssl ec -in key-ec-prime256v1-priv.pem -pubout -out key-ec-prime256v1-pub.pem
```

- Sign `"hello\n"`
```
echo hello | openssl pkeyutl -sign \
                             -inkey key-ec-prime256v1-priv.pem \
                             -rawin \
                             -digest sha256 \
           > hello-ec-prime256v1.sig
```
or (equivalent)
```
echo hello | openssl dgst -sign key-ec-prime256v1-priv.pem -sha256 > hello-ec-prime256v1.sig
```

- Verify `"hello\n"`
```
echo hello | openssl pkeyutl -verify \
                             -inkey key-ec-prime256v1-pub.pem -pubin \
                             -rawin \
                             -digest sha256 \
                             -sigfile hello-ec-prime256v1.sig
Signature Verified Successfully
```
or (equivalent):
```
echo hello | openssl dgst -verify key-ec-prime256v1-pub.pem -sha256 -signature hello-ec-prime256v1.sig
Verified OK
```

## Generate certificates:

Generate a self-signed certificate:

```
openssl req -x509 -key key-ec-prime256v1-priv.pem -out key-ec-prime256v1-cert.pem -subj "/CN=key-ec-prime256v1/" -days 3650
```
