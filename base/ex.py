import json
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Tạo cặp khóa RSA
def generate_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

# Tạo DID Document
def create_did_document(did, public_key):
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
    
    did_document = {
        "@context": "https://www.w3.org/ns/did/v1",
        "id": did,
        "verificationMethod": [{
            "id": f"{did}#keys-1",
            "type": "RsaVerificationKey2018",
            "controller": did,
            "publicKeyPem": public_key_pem
        }]
    }
    return did_document

# Ví dụ sử dụng
did = "did:example:123456789abcdefghi"
private_key, public_key = generate_key_pair()
did_document = create_did_document(did, public_key)

# Lưu tài liệu DID Document
with open("did_document.json", "w") as f:
    json.dump(did_document, f, indent=4)

print("DID Document created:", did_document)


# Code sinh DID và DID document 

