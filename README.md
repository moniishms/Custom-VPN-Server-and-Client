# Custom VPN Server and Client

## Description

This project implements a Python-based VPN system that enables secure communication between multiple systems connected over a hotspot or local network.  
It uses socket programming, AES encryption, and TUN/TAP interfaces to create an encrypted tunnel between a server and clients.  
This project is ideal for understanding low-level networking, encryption, and VPN concepts.

---

## Language & Dependencies

**Language:** Python 3  

**Libraries:**
- socket
- threading
- fcntl
- struct
- os
- time
- pycryptodome

**Dependency Manager:** pip

---

## Installation

### Step 1: Download and Install Ubuntu

Install Ubuntu using Oracle VM VirtualBox or on a physical PC.  
Download the latest LTS version from:  
`https://ubuntu.com/download/desktop`

For beginners, follow this video tutorial to install Ubuntu:  
**YouTube Setup Guide:** `https://www.youtube.com/watch?v=nCZcTKFbD2Q`

---

### Step 2: Set Up the Project

```bash
# Clone this repository
git clone https://github.com/moniishms/Custom-VPN-Server-and-Client.git
cd myvpn

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required dependencies
pip install pycryptodome
```

---

## Step 3: Usage

### Server Setup (Hotspot Host)

1. Enable the hotspot on your PC.  
   The default hotspot IP is typically `192.168.43.1`.

2. Start the server:

```bash
cd ~/myvpn
source venv/bin/activate
sudo python3 server.py
```

3. Keep the server terminal running. The server must remain active for clients to connect.

---

### Client Setup (Any PC Connected to Hotspot)

1. Edit `client.py` and replace the server IP with your hotspot IP:

```python
SERVER_IP = "192.168.43.1"  # Replace with your server’s hotspot IP
```

2. Run the client:

```bash
cd ~/myvpn
source venv/bin/activate
sudo python3 client.py
```

---

### Testing the VPN Connection

From the client terminal, test the VPN tunnel by pinging the server:

```bash
ping 10.8.0.1
```

If successful, you can also ping other clients connected to the same VPN network:

```bash
ping 10.8.0.2
```

---

## Project Structure

| File | Description |
|------|--------------|
| `server.py` | Initializes and manages the VPN server. Handles encryption, decryption, and data forwarding through TUN interface. |
| `client.py` | Connects to the VPN server via socket connection and establishes an encrypted tunnel using AES. |
| `README.md` | Documentation for setup, installation, and usage. |
| `venv/` | Virtual environment containing project dependencies. |

---

## Features

- AES-encrypted communication
- Socket-based data tunneling
- Works over hotspot or LAN
- Lightweight Python-based VPN
- Educational and easy to modify

---

## Troubleshooting

- **Permission Denied:** Run scripts using `sudo` to access `/dev/net/tun`.  
- **Module Not Found:** Ensure dependencies are installed inside the virtual environment.  
- **No Connection:** Make sure both server and client are on the same hotspot network.  
- **Ping Fails:** Disable firewall or check your network adapter configuration.

---

## Authors

**Moniish Mohansrinivasan**

---

## Optional

Provide your Ubuntu installation YouTube link here:  
`[Ubuntu Setup Video](https://www.youtube.com/watch?v=nCZcTKFbD2Q)`
