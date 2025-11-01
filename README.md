# MyVPN Hotspot Project

## Description
This project implements a Python-based VPN system that enables secure communication between multiple systems connected over a hotspot or local network. It uses socket programming, AES encryption, and TUN/TAP interfaces to create an encrypted tunnel between a server and clients. This project helps understand low-level networking, encryption, and VPN concepts.

## Language & Dependencies
Language: Python 3  
Libraries: socket, threading, fcntl, struct, os, time, pycryptodome  
Dependency Manager: pip

## Step 1: Install Ubuntu on VirtualBox
Download the latest LTS version of Ubuntu from https://ubuntu.com/download/desktop and install it using VirtualBox.

## Step 2: Configure VirtualBox Network Settings
To enable proper communication between your host (server) and guest (client) machines, configure two network adapters.

1. Shut down your Ubuntu VM if it’s running.
2. Open VirtualBox → Select your VM → Settings → Network.

**Adapter 1: NAT (for Internet Access)**
- Enable Network Adapter: Checked  
- Attached to: NAT  
- Purpose: Provides internet access inside the VM.

**Adapter 2: Bridged Adapter (for Local Hotspot Communication)**
- Enable Network Adapter: Checked  
- Attached to: Bridged Adapter  
- Name: Select your Wi-Fi adapter (the one used for your hotspot or connection)  
- Promiscuous Mode: Allow All  
- Cable Connected: Checked  

Click OK to save.

3. Restart the VM and verify interfaces
```
ip addr
```
You should see two interfaces, for example:
- enp0s3 – NAT (Internet)
- enp0s8 – Bridged (Hotspot communication)

4. Test connectivity
```
ping -c 4 google.com
ping 192.168.43.1
```
If both work, your network setup is correct.

## Step 3: Clone the Repository and Set Up the Project
```
sudo apt update
sudo apt install git python3-venv -y
git clone https://github.com/moniishmohan/Custom-VPN-Server-and-Client.git
cd Custom-VPN-Server-and-Client
python3 -m venv venv
source venv/bin/activate
pip install pycryptodome
```

## Step 4: Server Setup (Hotspot Host)
1. Enable your hotspot on the server PC (usually IP like `192.168.43.1`).
2. Start the VPN server:
```
cd ~/Custom-VPN-Server-and-Client
sudo ~/Custom-VPN-Server-and-Client/venv/bin/python3 server.py
```
Keep this terminal open. The server must remain active for clients to connect.

## Step 5: Client Setup (Hotspot Device)
1. Ensure the client PC is connected to the same hotspot as the server.
2. On the **server machine**, find its hotspot IP address:
```
ip addr
```
Look for the network interface connected to your hotspot (for example `wlp2s0` or `enp0s8`), and note the `inet` address.  
Example:
```
inet 192.168.43.1/24
```
Here, your server IP is `192.168.43.1`.

3. On the **client machine**, open the `client.py` file to edit it:
```
cd ~/Custom-VPN-Server-and-Client
nano client.py
```

4. Inside the file, find the following line:
```
SERVER_IP = "192.168.43.1"
```
Replace `"192.168.43.1"` with the server’s actual IP address obtained in Step 2.

5. Save and exit:
- Press `Ctrl + O` → Enter → `Ctrl + X`.

6. Start the client:
```
sudo ~/Custom-VPN-Server-and-Client/venv/bin/python3 client.py
```

## Step 6: Test the VPN Connection
On the client:
```
ping 10.8.0.1
ping 10.8.0.2
```
If packets are received, your encrypted tunnel is working.

## Troubleshooting
- **Permission Denied**: Run scripts with `sudo`.  
- **ModuleNotFoundError: No module named 'Crypto'**: Run `pip install pycryptodome` inside your virtual environment.  
- **Network Issues**: Check if both systems are on the same hotspot and the correct IP is set.  
- **TUN/TAP Errors**: Ensure you run with `sudo` and have TUN enabled in VirtualBox.  

## Project Structure
| File | Description |
|------|--------------|
| server.py | Handles encryption, tunneling, and packet forwarding. |
| client.py | Connects to server and sets up VPN tunnel. |
| README.md | Project documentation. |
| venv/ | Virtual environment folder. |

## Author
Moniish Mohansrinivasan  
Roll No: 24BCE5301
