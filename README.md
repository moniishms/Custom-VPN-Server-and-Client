MyVPN Hotspot Project
Description

This project implements a Python-based VPN system that enables secure communication between multiple systems connected over a hotspot or local network.
It uses socket programming, AES encryption, and TUN/TAP interfaces to create an encrypted tunnel between a server and clients.
This project is ideal for understanding low-level networking, encryption, and VPN concepts.

Language & Dependencies

Language: Python 3
Libraries:

socket

threading

fcntl

struct

os

time

pycryptodome

Dependency Manager: pip

Installation
Step 1: Download and Install Ubuntu

Install Ubuntu using Oracle VM VirtualBox or on a physical PC.
Download the latest LTS version from:
https://ubuntu.com/download/desktop

For beginners, follow this video tutorial to install Ubuntu:
YouTube Setup Guide: [Insert your YouTube installation link here]

Step 2: Set Up the Project
# Clone this repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd myvpn

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required dependencies
pip install pycryptodome

Usage
Server Setup (Hotspot Host)

Enable the hotspot on your PC.

The default hotspot IP is typically 192.168.43.1.

Start the server:

cd ~/myvpn
source venv/bin/activate
sudo python3 server.py


Keep the server terminal running. The server must remain active for clients to connect.

Client Setup (Any PC Connected to Hotspot)

Edit client.py and replace the server IP with your hotspot IP:

SERVER_IP = "192.168.43.1"  # Replace with your server’s hotspot IP


Run the client:

cd ~/myvpn
source venv/bin/activate
sudo python3 client.py

Testing the VPN Connection

From the client terminal, test the VPN tunnel by pinging the server:

ping 10.8.0.1


If successful, you can also ping other clients connected to the same VPN network (e.g., ping 10.8.0.2).

Project Structure
File	Description
server.py	Initializes and manages the VPN server. Handles encryption, decryption, and data forwarding through TUN interface.
client.py	Connects to the VPN server via socket connection and establishes an encrypted tunnel using AES.
README.md	Documentation for setup, installation, and usage.
venv/	Virtual environment containing project dependencies.
Authors

Moniish Mohansrinivasan