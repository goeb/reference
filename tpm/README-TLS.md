# Seal a private key and certificate in a TPM and use it for a TLS handshake 

This page assumes that the computer has a TPM.

## Setup

Requirements:
```
apt install tpm2-openssl
```


Create a private key:
```
sudo tpm2_createprimary --hierarchy o --hash-algorithm sha256 --key-algorithm rsa --key-context primary.ctx

sudo tpm2_create --parent-context primary.ctx --hash-algorithm sha256 --key-algorithm rsa --public key.pub --private key.priv

sudo tpm2_load --parent-context primary.ctx --public key.pub --private key.priv -c key.ctx

# Make the transient object persistent
sudo tpm2_evictcontrol --hierarchy o --object-context key.ctx 0x81010002
```

Create a certificate:
```
sudo openssl req -new -provider tpm2 \
  -key handle:0x81010002 \
  -out server.csr \
  -subj "/CN=test01"

# Make a self signed certificate
openssl x509 -req -days 365 -provider tpm2 -provider default \
  -in server.csr \
  -key handle:0x81010002 \
  -out server.crt
```

## TLS server and client

Start a minimal server:
```
openssl s_server \
  -provider tpm2 -provider default \
  -accept 8443 \
  -cert server.crt \
  -key handle:0x81010002
```

Start a minimal client:
```
openssl s_client -connect localhost:8443 -verify_return_error -CAfile server.crt
```

## Cleanup

```
sudo tpm2_evictcontrol -C o -c 0x81010002
persistent-handle: 0x81010002
action: evicted
```

