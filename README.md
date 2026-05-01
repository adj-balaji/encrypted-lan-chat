# 🔐 Encrypted LAN Chat & File Transfer System

## 🚀 Overview

This project implements a **secure LAN-based communication system** that supports:

* 💬 Encrypted messaging
* 📁 Secure file transfer
* 🔐 Hybrid encryption (AES + RSA)

It ensures that all communication between client and server is **confidential and protected from interception**.

---

## 🎯 Objective

To build a **secure peer-to-peer communication system** over a Local Area Network (LAN) using modern cryptographic techniques.

---

## 🔐 Security Architecture

* 🔑 **RSA (2048-bit)** → Secure key exchange
* 🔒 **AES (128-bit)** → Fast data encryption
* 📡 Socket Programming → Communication layer

---

## ⚙️ Features

* ✅ Encrypted real-time messaging
* ✅ Secure file transfer over LAN
* ✅ Hybrid encryption (RSA + AES)
* ✅ Multi-threaded communication
* ✅ Automatic key exchange
* ✅ File encryption before transfer

---

## 🧠 Tech Stack

* Python
* Socket Programming
* PyCryptodome (AES)
* RSA
* Threading

---

## 🏗️ System Architecture

```id="arch2"
Client                Server
  |                     |
  |---- Connect ------->|
  |<--- RSA Public Key--|
  |---- AES Key (Encrypted) --->|
  |                     |
  |==== Secure Communication ====|
  |   (AES Encrypted Data)      |
```

---

## 📂 Project Structure

```id="struct2"
Encrypted-LAN-Chat/
│
├── client.py
├── server.py
├── aes_utils.py
├── key_exchange.py
├── requirements.txt
├── README.md
```

---

## ▶️ Installation

```bash id="lan1"
git clone https://github.com/adj-balaji/encrypted-lan-chat.git
cd encrypted-lan-chat
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🖥️ Start Server

```bash id="lan2"
python server.py
```

### 💻 Start Client

```bash id="lan3"
python client.py
```

---

## 📡 How It Works

### 🔹 Step 1: Connection

* Client connects to server using sockets

### 🔹 Step 2: RSA Key Exchange

* Server generates RSA keys
* Public key sent to client
* Client encrypts AES key and sends back

👉 See implementation: 

---

### 🔹 Step 3: Secure Communication

* AES key used for:

  * Message encryption
  * File encryption

👉 Encryption logic: 

---

### 🔹 Step 4: Messaging

* Messages are encrypted before sending
* Decrypted on receiver side

👉 Client handling: 

---

### 🔹 Step 5: File Transfer

* Files encrypted using AES
* Sent as binary
* Decrypted after receiving

👉 Server handling: 

---

## 📊 Key Concepts

* 🔐 Hybrid Encryption
* 🔄 Client-Server Architecture
* ⚡ Multi-threading
* 📡 Socket Communication

---

## 📌 Example Flow

1. Run server
2. Run client
3. Choose:

   * Send message
   * Send file
4. Data gets encrypted → transmitted → decrypted

---

## ⚠️ Limitations

* Supports single client connection
* Works only within LAN
* No GUI (CLI-based)

---

## 🚀 Future Enhancements

* 🌐 Multi-client support
* 🖥️ GUI (Tkinter / Web UI)
* 🔑 End-to-end authentication
* ☁️ Internet-based communication
* 📱 Mobile integration

---

## 👨‍💻 Author

**BALAJI A D J**
GitHub: https://github.com/adj-balaji

---

## ⭐ Star this repo if you like it!
