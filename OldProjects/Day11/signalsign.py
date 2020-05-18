import os
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives import serialization, hashes, padding
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
import json


DEFAULT_BACKEND = default_backend()
CLIENT_PASSWORD = None
SALT = os.urandom(16)
SIGNATURE_FOR_PRE_KEY = None
ROOT_KEY = None
NONCE = os.urandom(12)
DEFAULT_PAD_QUANTUM = 128


def gen_root_key():
    key = ChaCha20Poly1305.generate_key()
    key_cha = ChaCha20Poly1305(key)
    return key, key_cha

def make_key_pair():
    private_key = ed25519.Ed25519PrivateKey.generate()
    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )
    #loaded_private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_bytes)

    public_key = private_key.public_key()
    public_bytes = public_key.public_bytes(
                                        encoding = serialization.Encoding.Raw,
                                        format = serialization.PublicFormat.Raw
    )
    #loaded_public_key = ed25519.Ed25519PublicKey.from_public_bytes(public_bytes)
    return private_bytes,public_bytes

def encrypts(chacha,data,data2):
    return chacha.encrypt(NONCE,data,data2)

def sha256( data ):
    h = hashes.Hash( hashes.SHA256(), backend=DEFAULT_BACKEND )
    h.update( data )
    return h.finalize()

def kdf_scrypt(password):
    kdf = Scrypt(
        salt=SALT,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=DEFAULT_BACKEND
    )
    key = kdf.derive(password)
    return key

def encrypt_things(data,key):
    algorithm = algorithms.ChaCha20(key, SALT)
    cipher = Cipher(
        algorithm,
        mode=None,
        backend=DEFAULT_BACKEND
    )
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

def main():
    id = make_key_pair()
    pre_key = make_key_pair()

    loaded_private_key = ed25519.Ed25519PrivateKey.from_private_bytes(id[1])

    signature = loaded_private_key.sign(sha256((pre_key[0])))

    password = bytes.fromhex('898974')
    key = kdf_scrypt(password)

    root_key, key_cha = gen_root_key()
    #ct = key_cha.encrypt(NONCE,root_key,None)
    f = encrypt_things(root_key,key)

    associated_data = [
        SALT.hex(),
        NONCE.hex(),
        id[1].hex(),
        pre_key[1].hex(),
        signature.hex(),
        f.hex()
    ]

    encrypted_data = [
        #padandEncrypt(id[0],key).hex(),
        #padandEncrypt(pre_key[0],key).hex()
        id[0].hex(),
        pre_key[0].hex()

    ]

    a = json.dumps(associated_data)
    b = json.dumps(encrypted_data).encode()
    b2 = key_cha.encrypt(NONCE,b,a.encode()).hex()
    return a, b2


print(main())
