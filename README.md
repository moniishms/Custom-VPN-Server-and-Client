# Custom VPN Server and Client
**Author:** Moniish Mohansrinivasan  
**Roll No:** 24BCE5301  

---

## Project Description
This project implements a lightweight **custom VPN system** in Python that enables secure and encrypted communication between multiple systems connected through a hotspot or local network.

It uses **socket programming**, **AES encryption**, and **TUN/TAP interfaces** to create a virtual tunnel between a VPN server and multiple clients.  
The project demonstrates key concepts of tunneling, encryption, and virtual networking.

---

## Technologies Used
- **Language:** Python 3  
- **Core Libraries:**  
- `socket`  
- `threading`  
- `fcntl`  
- `struct`  
- `os`  
- `time`  
- `pycryptodome`  
- **Dependency Manager:** `pip`

---

## Installation

### Step 1: Install Ubuntu
You can install Ubuntu using **Oracle VM VirtualBox** or directly on a physical PC.  
Download the latest LTS version here:  
🔗 [Ubuntu Official Download](https://ubuntu.com/download/desktop)

For beginners, you may refer to this tutorial:  
🎥 [YouTube: How to Install Ubuntu](https://www.youtube.com/watch?v=nCZcTKFbD2Q)

---

### Step 2: Clone the Repository
Open the Ubuntu terminal and run:
```bash
sudo apt update
sudo apt install git -y
git clone https://github.com/moniishms/Custom-VPN-Server-and-Client.git
cd Custom-VPN-Server-and-Client
Step 3: Set Up Virtual Environment and Dependencies
bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install pycryptodome
Usage
Server Setup (Hotspot Host)
Enable hotspot on your PC (default IP usually 192.168.43.1).

Start the VPN server:

bash
Copy code
cd ~/Custom-VPN-Server-and-Client
source venv/bin/activate
sudo python3 server.py
Keep the server terminal open — it must remain active for client connections.

Client Setup (Any PC Connected to Hotspot)
Edit client.py and set your server IP:

python
Copy code
SERVER_IP = "192.168.43.1"  # Replace with your server’s hotspot IP
Run the client:

bash
Copy code
cd ~/Custom-VPN-Server-and-Client
source venv/bin/activate
sudo python3 client.py
Testing the VPN Connection
From the client terminal:

bash
Copy code
ping 10.8.0.1
If the connection is successful, you can also test connectivity between multiple clients:

bash
Copy code
ping 10.8.0.2
Project Structure
File	Description
server.py	Initializes and manages the VPN server. Handles encryption, decryption, and data forwarding through the TUN interface.
client.py	Connects to the VPN server and establishes an encrypted communication tunnel using AES.
README.md	Documentation for setup, installation, and usage.
venv/	Virtual environment containing project dependencies.