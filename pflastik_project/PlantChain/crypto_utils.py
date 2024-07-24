from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key, Encoding, PrivateFormat, PublicFormat, NoEncryption
from cryptography.hazmat.backends import default_backend

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def serialize_private_key(private_key):
    return private_key.private_bytes(
        encoding=Encoding.PEM,
        format=PrivateFormat.PKCS8,
        encryption_algorithm=NoEncryption()
    ).decode('utf-8')

def serialize_public_key(public_key):
    return public_key.public_bytes(
        encoding=Encoding.PEM,
        format=PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')

def sign_data(private_key, data):
    return private_key.sign(
        data.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def verify_signature(public_key, data, signature):
    try:
        public_key.verify(
            signature,
            data.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False

# Example usage:

# 1. Generate a key pair
private_key, public_key = generate_key_pair()

# 2. Serialize the keys
private_key_pem = serialize_private_key(private_key)
public_key_pem = serialize_public_key(public_key)
print("Private Key:")
print(private_key_pem)
print("\nPublic Key:")
print(public_key_pem)

# 3. Sign some data
data = "This is a test message."
signature = sign_data(private_key, data)
print("\nSignature:")
print(signature)

# 4. Verify the signature
is_valid = verify_signature(public_key, data, signature)
print("\nIs the signature valid?")
print(is_valid)

# Deserialization example (optional):
# Load the private and public key from the PEM formatted strings
private_key = load_pem_private_key(private_key_pem.encode('utf-8'), password=None, backend=default_backend())
public_key = load_pem_public_key(public_key_pem.encode('utf-8'), backend=default_backend())

# Verify again after deserialization
is_valid_after_deserialization = verify_signature(public_key, data, signature)
print("\nIs the signature valid after deserialization?")
print(is_valid_after_deserialization)


# Serialized keys (PEM format)
private_key_pem = """
-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDLrtyYHF2dlO+d
/dpsMkqitmXMkB7UBQh6YWbEqI4saWZsV6xL7UFsiZP/I3cSdP/7FA7IY/Sz7ve1
pqqhCGEun53z0k5GRyrBILUw4UJc5e9HbNp/4aAyIuno7SO98JoGe6K3V4st2n9/
13VAssFCyys/ELRr6m6ZWk0pa971PWZ9S0BJEUQDc8avCPpjCvcQKAs1LGqqZUGi
aEK9M/aawVH+3gktXE4tLQD0LOBTMoybbt0yHef968Pfibj+QDPnNWoHGLnaM/jT
Ch2dTWAoTH+CcAdf0qKAyWZ7eD6n1PPWD+I2qc35HZ17XpLDoWz49z+e2xVZEzN1
+acn51ufAgMBAAECggEAB8yzMQMrdcFVe6m6feVfHkpfYGBhQQhmtRw0INiJ7GfZ
pQRzQJhEc330Z0ZZ/obxPN6DwmcX4I87q36tjtHdugW6uRkW9KUwNr0KszITcuM+
ZAnMqpQrqKY8A5z95WQbqDiyMaGHxUKJgPSLNOY9DrjtxJ7eVqBfij4yMW5ECp5o
M1BnG476Wn2KLAvlOfDpxjqFWlpTiLnY5tdHb5y6Je97z4ilIH8dLwNc+IuDay6R
Ht51vUM5R8jYF93l8pW/jwn1fcLBQtkaPTkjtzFlenaiv+9QbGPgNmSwGqwRNB+/
qu84tV6lKvokHpp4E3tX63FhTPFQQi0yDr3sOzSIwQKBgQDrLfuSurwQplYb4WpI
3rGJ+Mete3jO0NvTjcPjdCN84U3B7t/RSJEV1JT9YPQ77pLXrbahkZ95nnuU7w76
AmurKpBViHlD7/cBXTT6GZc5U3wuslwMwJ0QjDvuGI7fo73nqy5x0LVHFSZUEDFB
72SfpQAexBaIwsqe5jXIc0fZhwKBgQDdtw2n7dg6o+E18aRwc89LjpLXeZds3AHg
6Z3wFknUHiaXwIsV6Rgqvt9r4LK6uSEFvGPz7EowNUaTkcaeSrF4LAvZr1Ei67X1
wQ4/zE9CQ/NIY9IBGVgHPMOlqWb596uXxH757T5JB8e4fa63IMMbJCyrBcCsOIhK
jP4UH9uTKQKBgQC0IctALsEfa5gm0LgMym1nxWKD0T/OARFu73WrwOfxncxmD2Xl
MdTWyLW5gUpwoSJeClMJW7WvfKEhiR2KhtIbD4XvzZE8ZQ9nPxH1wiYfJX/HcJuq
tNlYtGCu1KaSSyOIz4fKa1Z99Igf+SsRWqBS2xnFduHfrHtvy9pEB3Bv/wKBgQCh
k/MGy+YGLkJFftnY/f03Uisfj0RUmC1iTL7GJmgdhu+XLkHucNYk6L+ILdPzElHH
jVjGfhA++8R4bQdzennFW0wzk3ms2lzcQZpx0iJ852pX+i8kj+TAOX9XrpIWX3GV
BCWJXGVE8b+Saz21xdGKaR2IcYPNvtFMi13rKqBpqQKBgQDXN+WBaaaLWyeaLMfD
PXe+7hAkziBGSldiaGiIxuoKTRHjUbdxqFosj/AjaPeaXoK5Vs83WywSuaywYvP8
LQwHt3Qvo2SHj2F+3vzJmOmpnCUExbnfU90/9iMyH9z6r+C/TrSHEObDKI3XVvPb
zGRjMO3WBhR35rCKPWV4ygRNnQ==
-----END PRIVATE KEY-----
"""

public_key_pem = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy67cmBxdnZTvnf3abDJK
orZlzJAe1AUIemFmxKiOLGlmbFesS+1BbImT/yN3EnT/+xQOyGP0s+73taaqoQhh
Lp+d89JORkcqwSC1MOFCXOXvR2zaf+GgMiLp6O0jvfCaBnuit1eLLdp/f9d1QLLB
QssrPxC0a+pumVpNKWve9T1mfUtASRFEA3PGrwj6Ywr3ECgLNSxqqmVBomhCvTP2
msFR/t4JLVxOLS0A9CzgUzKMm27dMh3n/evD34m4/kAz5zVqBxi52jP40wodnU1g
KEx/gnAHX9KigMlme3g+p9Tz1g/iNqnN+R2de16Sw6Fs+Pc/ntsVWRMzdfmnJ+db
nwIDAQAB
-----END PUBLIC KEY-----
"""

# Load the private and public key from the PEM formatted strings
private_key = load_pem_private_key(private_key_pem.encode('utf-8'), password=None, backend=default_backend())
public_key = load_pem_public_key(public_key_pem.encode('utf-8'), backend=default_backend())

# Example data to sign
data = "This is a test message."

# Sign the data
signature = sign_data(private_key, data)
print("\nSignature:")
print(signature)

# Verify the signature
is_valid = verify_signature(public_key, data, signature)
print("\nIs the signature valid?")
print(is_valid)
