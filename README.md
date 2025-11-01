# Custom VPN Server and Client

**Author:** Mohan Srinivasan Moniish  
**Roll No:** 24BCE5301  

---

## Project Overview

This project implements a custom VPN server and client using Python socket programming and AES encryption.  
It securely tunnels network traffic between connected systems through a virtual network interface (TUN device).

One Ubuntu machine acts as the VPN server (hotspot host), and other systems connect as clients.  
Together, they form an encrypted private network that functions over a hotspot or LAN connection.

---

## Features

- Encrypted communication using AES (EAX mode)  
- Custom VPN tunnel using `/dev/net/tun`  
- Cross-system communication through hotspot or LAN  
- Multiple clients supported  
- Lightweight and easy to configure  
- Tested on Ubuntu 22.04 and above

---

## Learn Ubuntu Setup

You can refer to this space to add a YouTube tutorial link for installing and configuring Ubuntu.  
*(Example placeholder: [YouTube Link – How to Install Ubuntu](#))*

---

## Prerequisites

Before proceeding, ensure the following:

- Ubuntu installed (native or via VirtualBox)
- Python 3.8 or higher installed
- pip package manager installed
- Working internet connection or local hotspot

---

## Understanding Hotspot Setup

When your Ubuntu server acts as a hotspot:
- The server gets a local IP (for example: `192.168.43.1`)  
- Clients connected to the hotspot receive IPs in the same subnet (e.g., `192.168.43.10`)

In `client.py`, update the following line to match your server’s hotspot IP:
```python
SERVER_IP = "192.168.43.1"  # Replace with your server hotspot IP
Setup Steps
1. Clone the Repository
On Ubuntu, open the terminal and run:

bash
Copy code
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
2. Create a Virtual Environment
bash
Copy code
sudo apt update
sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install pycryptodome
4. File Transfer (if needed)
If cloning is not used, you can download the files manually:

Upload server.py and client.py to GitHub.

In Ubuntu, open a browser, download the files, and move them to your project folder:

bash
Copy code
mv ~/Downloads/server.py ~/myvpn/
mv ~/Downloads/client.py ~/myvpn/
Make them executable:

bash
Copy code
chmod +x server.py client.py
Running the VPN
Server (Hotspot Host)
On the server machine (hotspot PC), run:

bash
Copy code
cd ~/myvpn
source venv/bin/activate
sudo python3 server.py
Keep this terminal open. The VPN server must remain active while clients connect.

Client (Connected Machine)
On the client system connected to the hotspot:

Edit the client.py file and replace the IP:

python
Copy code
SERVER_IP = "192.168.43.1"
Run the following commands:

bash
Copy code
cd ~/myvpn
source venv/bin/activate
sudo python3 client.py
Testing Connectivity
From the client machine, test the VPN tunnel:

bash
Copy code
ping 10.8.0.1   # Ping the server VPN IP
If responses are received, the VPN tunnel is active and data is encrypted successfully.

Troubleshooting
Issue	Possible Cause	Solution
PermissionError: [Errno 13]	Script not run as root	Use sudo python3 server.py
ConnectionRefusedError	Server not started or incorrect IP	Check SERVER_IP and restart server
ping fails	VPN interface not configured	Verify TUN setup permissions
ModuleNotFoundError	Missing library	Run pip install pycryptodome

File Structure
bash
Copy code
.
├── README.md         # Setup and usage guide
├── server.py         # VPN Server script
└── client.py         # VPN Client script
License
This project was developed as part of an academic submission.
It may be used or referenced for educational purposes.

Credits
Developed by: Mohan Srinivasan Moniish (24BCE5301)
Department of Computer Science and Engineering