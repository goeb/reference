
# Ref: https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

import binascii
import cryptography.hazmat.primitives.asymmetric.rsa
import cryptography.hazmat.primitives.serialization

private_key = cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

private_pem = private_key.private_bytes(
    encoding=cryptography.hazmat.primitives.serialization.Encoding.PEM,
    format=cryptography.hazmat.primitives.serialization.PrivateFormat.PKCS8,
    encryption_algorithm=cryptography.hazmat.primitives.serialization.NoEncryption()
)

print('private_pem:', private_pem)

public_key = private_key.public_key()
public_pem = public_key.public_bytes(
   encoding=cryptography.hazmat.primitives.serialization.Encoding.PEM,
   format=cryptography.hazmat.primitives.serialization.PublicFormat.SubjectPublicKeyInfo
)
print('public_pem:', public_pem)

# Sign a message

message = b"hello\n"
print("message:", message)

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("signature:", binascii.hexlify(signature))

for message in [b"hello\n", b"hello2\n"]:
    print("Verifying message=%s" % message)
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print('OK')
    except cryptography.exceptions.InvalidSignature:
        print('ERROR')






