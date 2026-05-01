import socket, threading, os, rsa
from aes_utils import *
from key_exchange import *

SERVER_IP, PORT = '192.168.1.2', 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM); client.connect((SERVER_IP, PORT))
print("[+] Connected to server.")

# Key exchange
aes_key = generate_aes_key()
client.send(encrypt_key_with_rsa(aes_key, rsa.PublicKey.load_pkcs1(client.recv(2048))))
print("[+] AES key sent securely.")

def receive():
    try:
        while True:
            header = client.recv(5).decode()
            if header == "MSG::": print("[Server]:", decrypt_message(client.recv(4096).decode(), aes_key))
            elif header == "FILE:":
                fname = client.recv(int.from_bytes(client.recv(2),'big')).decode()
                size, data = int.from_bytes(client.recv(8),'big'), b""
                while len(data) < size: data += client.recv(4096)
                with open(f"received_{fname}", 'wb') as f: f.write(decrypt_file(data, aes_key))
                print(f"[+] Received file saved as received_{fname}")
    except: print("[-] Disconnected.")

def send():
    while True:
        c = input("1. Send Message\n2. Send File\n>> ")
        if c == '1': client.send(b"MSG::"); client.send(encrypt_message(input("Enter message: "), aes_key).encode())
        elif c == '2':
            path = input("Enter full file path: ")
            if not os.path.exists(path): print("[-] File not found!"); continue
            enc, fname = encrypt_file(path, aes_key), os.path.basename(path)
            client.send(b"FILE:"); client.send(len(fname).to_bytes(2,'big')); client.send(fname.encode())
            client.send(len(enc).to_bytes(8,'big')); client.sendall(enc); print("[+] File sent.")

threading.Thread(target=receive).start(); send()
