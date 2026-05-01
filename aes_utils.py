from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

def generate_aes_key():
    return os.urandom(16)  # 128-bit AES key

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode()
    ct = base64.b64encode(ct_bytes).decode()
    return iv + ":" + ct

def decrypt_message(enc_message, key):
    iv, ct = enc_message.split(":")
    cipher = AES.new(key, AES.MODE_CBC, base64.b64decode(iv))
    pt = unpad(cipher.decrypt(base64.b64decode(ct)), AES.block_size)
    return pt.decode()

def encrypt_file(filepath, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    with open(filepath, 'rb') as f:
        data = pad(f.read(), AES.block_size)
        encrypted = cipher.encrypt(data)
    return iv + encrypted  # raw bytes

def decrypt_file(encrypted_data, key):
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return decrypted
