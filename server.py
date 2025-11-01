"""Author: Moniish Mohansrinivasan
Usage:
    sudo python3 server.py
"""

import socket
from Crypto.Cipher import AES
import threading
import fcntl
import struct
import os
import time

KEY = b"ThisIsASecretKey"
clients = {}

# TUN setup
IFF_TUN = 0x0001
IFF_NO_PI = 0x1000
TUNSETIFF = 0x400454ca

tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'tun0', IFF_TUN | IFF_NO_PI)
fcntl.ioctl(tun, TUNSETIFF, ifr)

os.system("ip addr add 10.8.0.1/24 dev tun0")
os.system("ip link set tun0 up")
print("[+] Server TUN device ready")


def encrypt(data):
    cipher = AES.new(KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext


def decrypt(data):
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)


def handle_client(conn, addr, client_ip):
    print(f"[+] Client connected {addr} → {client_ip}")
    conn.send(client_ip.encode())
    clients[conn] = client_ip
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            packet = decrypt(data)
            os.write(tun, packet)
    except Exception as e:
        print(f"[!] Error with {addr}: {e}")
    finally:
        clients.pop(conn, None)
        conn.close()
        print(f"[-] Client disconnected {addr}")


def tun_reader():
    while True:
        packet = os.read(tun, 4096)
        for c in list(clients.keys()):
            try:
                c.send(encrypt(packet))
            except:
                clients.pop(c, None)
        time.sleep(0.01)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen(5)
print("[+] Server listening on port 9999")

threading.Thread(target=tun_reader, daemon=True).start()

base_ip = 2

while True:
    conn, addr = server.accept()
    client_ip = f"10.8.0.{base_ip}"
    base_ip += 1
    threading.Thread(target=handle_client, args=(conn, addr, client_ip)).start()
