import socket
import threading
import os
from aes_utils import *
from key_exchange import *

HOST = '0.0.0.0'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"[+] Waiting for connection on port {PORT}...")

conn, addr = server.accept()
print(f"[+] Connected with {addr}")

# RSA key exchange
pub_key, priv_key = generate_rsa_keys()
conn.send(pub_key.save_pkcs1("PEM"))
enc_key = conn.recv(2048)
aes_key = decrypt_key_with_rsa(enc_key, priv_key)
print("[+] AES key exchanged securely.")

def receive():
    while True:
        try:
            header = conn.recv(5).decode()
            if header == "MSG::":
                msg = conn.recv(4096).decode()
                print("[Client]:", decrypt_message(msg, aes_key))
            elif header == "FILE:":
                filename_len = int.from_bytes(conn.recv(2), 'big')
                filename = conn.recv(filename_len).decode()
                file_size = int.from_bytes(conn.recv(8), 'big')
                encrypted_data = b""
                while len(encrypted_data) < file_size:
                    encrypted_data += conn.recv(4096)
                content = decrypt_file(encrypted_data, aes_key)
                with open(f"received_{filename}", 'wb') as f:
                    f.write(content)
                print(f"[+] Received file saved as received_{filename}")
        except:
            print("[-] Connection closed.")
            break

def send():
    while True:
        choice = input("1. Send Message\n2. Send File\n>> ")
        if choice == '1':
            msg = input("Enter message: ")
            enc_msg = encrypt_message(msg, aes_key)
            conn.send(b"MSG::")
            conn.send(enc_msg.encode())
        elif choice == '2':
            filepath = input("Enter full file path: ")
            if not os.path.exists(filepath):
                print("[-] File not found!")
                continue
            enc_data = encrypt_file(filepath, aes_key)
            filename = os.path.basename(filepath)
            conn.send(b"FILE:")
            conn.send(len(filename).to_bytes(2, 'big'))
            conn.send(filename.encode())
            conn.send(len(enc_data).to_bytes(8, 'big'))
            conn.sendall(enc_data)
            print("[+] File sent.")
threading.Thread(target=receive).start()
send()
