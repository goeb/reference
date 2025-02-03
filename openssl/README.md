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
           > hello-ec-prime256v1.sig
```

- Verify `"hello\n"`
```
echo hello | openssl pkeyutl -verify \
                             -inkey key-ec-prime256v1-pub.pem -pubin \
                             -sigfile hello-ec-prime256v1.sig
Signature Verified Successfully
```
