#!/usr/bin/env python3
"""
client.py – Secure VPN Client over AES-encrypted TCP Tunnel

This script connects to a VPN server, sets up a TUN interface,
and securely transmits encrypted packets between client and server.

Author: Moniish Mohansrinivasan
Usage:
    sudo python3 client.py
"""

import socket
from Crypto.Cipher import AES
import fcntl
import struct
import os
import select
import time

# --- Encryption Key ---
KEY = b"ThisIsASecretKey"

# --- AES Encryption & Decryption Functions ---
def encrypt(data):
    cipher = AES.new(KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext

def decrypt(data):
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

# --- TUN Device Setup ---
IFF_TUN = 0x0001
IFF_NO_PI = 0x1000
TUNSETIFF = 0x400454ca

tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'tun1', IFF_TUN | IFF_NO_PI)
fcntl.ioctl(tun, TUNSETIFF, ifr)
os.system("ip link set tun1 up")
print("[+] Client TUN device ready")

# --- Server Connection ---
server_ip = "127.0.0.1"  # Replace with your server’s IP or hotspot IP
server_port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))
client_ip = s.recv(12).decode().strip()
os.system(f"ip addr add {client_ip}/24 dev tun1")
print(f"[+] Connected to server {server_ip}:{server_port} → Assigned IP: {client_ip}")

# --- Main Data Loop ---
tun_sockets = [tun, s]

while True:
    readables, _, _ = select.select(tun_sockets, [], [], 1.0)
    for fd in readables:
        if fd == tun:
            packet = os.read(tun, 4096)
            s.send(encrypt(packet))
        else:
            data = s.recv(4096)
            if data:
                packet = decrypt(data)
                os.write(tun, packet)
    time.sleep(0.01)
