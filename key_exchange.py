import rsa
import base64

def generate_rsa_keys():
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

def encrypt_key_with_rsa(aes_key, public_key):
    encrypted = rsa.encrypt(aes_key, public_key)
    return base64.b64encode(encrypted)

def decrypt_key_with_rsa(encrypted_key_b64, private_key):
    encrypted_key = base64.b64decode(encrypted_key_b64)
    return rsa.decrypt(encrypted_key, private_key)
