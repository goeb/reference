#!/usr/bin/env python3

"""
This program builds the following certificate chain:

    01-root-ca-cert.pem
    +-- 02-intermediate-ca-cert.pem
        +-- 03-user-cert.pem

And does verifications about which authenticates which.
"""

import datetime
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes


def verify_cert(user_cert, ca_cert):
    """Verify if a subordinate certificate is issued by a CA certificate"""
    with open(user_cert, 'rb') as user_fd, open(ca_cert, 'rb') as ca_fd:
        cert_issuer = x509.load_pem_x509_certificate(ca_fd.read())
        cert_to_check = x509.load_pem_x509_certificate(user_fd.read())
    issuer_public_key = cert_issuer.public_key()
    cert_to_check.verify_directly_issued_by(cert_issuer)


def serialize_private_key(output_path, key):
    """Write a private key to a file"""
    private_key_data = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    with open(output_path, "wb") as f:
        f.write(private_key_data)
    print(f"created private key: {output_path}")


def create_rsa_key(output_path):
    """Create a RSA private key"""
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048,)
    serialize_private_key(output_path, key)


def create_ec_key(output_path):
    """Create an EC private key"""
    key = ec.generate_private_key(ec.SECP256R1())
    serialize_private_key(output_path, key)


def generate_csr(output_path, private_key):
    """Generate a CSR"""
    csr = x509.CertificateSigningRequestBuilder()
    csr = csr.subject_name(x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, "mysite.com"),
    ]))
    # Sign the CSR with our private key.
    csr = csr.sign(private_key, hashes.SHA256())
    # Serialize and write to file
    with open(output_path, "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))


def load_private_key(input_path):
    """Load a private key from file"""
    with open(input_path, "rb") as f:
        key_data = f.read()
    return serialization.load_pem_private_key(key_data, None)


def generate_self_signed_cert(output_path, private_key):
    """Generate a self-signed certificate"""
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, "root ca"),
    ])
    cert = x509.CertificateBuilder()
    cert = cert.subject_name(subject)
    cert = cert.issuer_name(issuer)
    cert = cert.public_key(private_key.public_key())
    cert = cert.serial_number(0x112233445566778899)
    cert = cert.not_valid_before(datetime.datetime(2024, 1, 1, 15, 55))
    cert = cert.not_valid_after(datetime.datetime(2054, 12, 25, 14, 44))
    # Sign our certificate with our private key
    cert = cert.sign(private_key, hashes.SHA256())
    with open(output_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    print(f"generated self-signed certificate: {output_path}")


def generate_certificate(output_path, common_name, key, ca_cert, ca_key):
    """Generate a certificate, signed by a CA"""
    subject = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, common_name),
    ])
    cert = x509.CertificateBuilder()
    cert = cert.subject_name(subject)
    cert = cert.issuer_name(ca_cert.subject)
    cert = cert.public_key(key.public_key())
    cert = cert.serial_number(x509.random_serial_number())
    cert = cert.not_valid_before(datetime.datetime(2024, 2, 2, 11, 11))
    cert = cert.not_valid_after(datetime.datetime(2053, 12, 23, 13, 33))
    cert = cert.add_extension(
        x509.SubjectKeyIdentifier.from_public_key(key.public_key()),
        critical=False,
    )
    cert = cert.add_extension(
        x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_key.public_key()),
        critical=False,
    )
    # Sign our certificate with our private key
    cert = cert.sign(ca_key, hashes.SHA256())
    with open(output_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    print(f"generated certificate: {output_path}")


# main

# Root CA
create_rsa_key("01-root-ca-key.pem")
root_ca_key = load_private_key("01-root-ca-key.pem")
generate_self_signed_cert("01-root-ca-cert.pem", root_ca_key)
root_ca_cert = x509.load_pem_x509_certificate(open("01-root-ca-cert.pem", "rb").read())

# Intermediate CA
create_ec_key("02-intermediate-ca-key.pem")
intermediate_ca_key = load_private_key("02-intermediate-ca-key.pem")
generate_certificate("02-intermediate-ca-cert.pem", "intermediate ca", intermediate_ca_key, root_ca_cert, root_ca_key)
intermediate_ca_cert = x509.load_pem_x509_certificate(open("02-intermediate-ca-cert.pem", "rb").read())

# User (leaf) certificate
create_rsa_key("03-user-key.pem")
user_key = load_private_key("03-user-key.pem")
generate_certificate("03-user-cert.pem", "user", user_key, intermediate_ca_cert, intermediate_ca_key)

# Verify 
verify_cert("03-user-cert.pem", "02-intermediate-ca-cert.pem")
verify_cert("02-intermediate-ca-cert.pem", "01-root-ca-cert.pem")
verify_cert("01-root-ca-cert.pem", "01-root-ca-cert.pem")
try:
    verify_cert("03-user-cert.pem", "01-root-ca-cert.pem")
except ValueError as e:
    print("expected error 1: %s" % e)
