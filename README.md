# MyVPN Hotspot Project

## Description
This project implements a Python-based VPN system that enables secure communication between multiple systems connected over a hotspot or local network. It uses socket programming, AES encryption, and TUN/TAP interfaces to create an encrypted tunnel between a server and clients. This project helps understand low-level networking, encryption, and VPN concepts.

## Language & Dependencies
- **Language:** Python 3  
- **Libraries:** socket, threading, fcntl, struct, os, time, pycryptodome  
- **Dependency Manager:** pip  

## Step 1: Install Ubuntu on VirtualBox
Download the latest LTS version of Ubuntu from:  
[https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)

You can install Ubuntu using Oracle VM VirtualBox.  
Follow a YouTube guide if needed:  
[Ubuntu Installation Video Guide](https://www.youtube.com/watch?v=nCZcTKFbD2Q)

---

## Step 2: Configure VirtualBox Network Settings
To enable proper communication between your host (server) and guest (client) machines, configure **two network adapters**.

1. **Shut down** your Ubuntu VM if it’s running.  
2. Open **VirtualBox → Select your VM → Settings → Network.**

### Adapter 1: NAT (Internet Access)
- Enable Network Adapter: ✅  
- Attached to: NAT  
- Purpose: Provides internet access inside the VM.

### Adapter 2: Bridged Adapter (Hotspot Communication)
- Enable Network Adapter: ✅ 
- Attached to: Bridged Adapter  
- Name: Select your Wi-Fi adapter (used for hotspot connection)  
- Promiscuous Mode: Allow All  
- Cable Connected: ✅  

Click **OK** to save.

3. **Restart** the VM and verify interfaces:
```bash
ip addr
```

You should see two interfaces, for example:

- enp0s3 – NAT (Internet)  
- enp0s8 – Bridged (Hotspot)

### Test Connectivity
```bash
ping -c 4 google.com
ping 192.168.43.1
```

If both commands succeed, your VM network setup is correct.

## Step 3: Clone the Repository and Set Up the Project
```bash
sudo apt update
sudo apt install git python3-venv -y
git clone https://github.com/moniishms/Custom-VPN-Server-and-Client.git
cd Custom-VPN-Server-and-Client
python3 -m venv venv
source venv/bin/activate
pip install pycryptodome
```

## Step 4: Server Setup (Hotspot Host)

Enable your hotspot on the server PC (it usually has IP 192.168.43.1).

Start the VPN server:
```bash
cd ~/Custom-VPN-Server-and-Client
sudo ~/Custom-VPN-Server-and-Client/venv/bin/python3 server.py
```

Keep this terminal running — the server must remain active for clients to connect.

## Step 5: Client Setup (Hotspot Device)

Ensure the client PC is connected to the same hotspot as the server.

On the server machine, find its hotspot IP address:
```bash
ip addr
```

Look for the interface connected to the hotspot (for example wlp2s0 or enp0s8) and note its inet address:  
Example output:
```
inet 192.168.43.1/24
```

Here, your server IP is `192.168.43.1`.

On the client machine, open the client script:
```bash
cd ~/Custom-VPN-Server-and-Client
nano client.py
```

Inside the file, modify the following line:
```python
SERVER_IP = "192.168.43.1"
```

Replace `192.168.43.1` with the actual server IP obtained from the previous step.

Save and exit:  
Press `Ctrl + O`, hit `Enter`, then press `Ctrl + X`.

Start the client:
```bash
sudo ~/Custom-VPN-Server-and-Client/venv/bin/python3 client.py
```

## Step 6: Test the VPN Connection

Once both the server and client are running:

On the client machine, test the encrypted VPN connection:
```bash
ping 10.8.0.1
ping 10.8.0.2
```

If packets are received, the VPN tunnel is active and working correctly.

## Troubleshooting

| Issue                                      | Cause                     | Solution                                                                 |
|-------------------------------------------|---------------------------|--------------------------------------------------------------------------|
| Permission denied                         | Lacking root privileges   | Run commands with `sudo`.                                                |
| ModuleNotFoundError: No module named 'Crypto' | Dependency missing        | Run `pip install pycryptodome` inside your virtual environment.          |
| Network unreachable                       | Hotspot misconfiguration  | Ensure both systems are on the same hotspot and correct IP is set.       |
| TUN/TAP errors                            | Missing permissions       | Run with `sudo` and make sure TUN is enabled in VirtualBox settings.     |

## Project Structure

| File        | Description                                                  |
|-------------|--------------------------------------------------------------|
| server.py   | Handles AES encryption, tunneling, and packet forwarding.    |
| client.py   | Connects to the VPN server and establishes an encrypted tunnel. |
| README.md   | Project documentation.                                       |
| venv/       | Python virtual environment containing project dependencies.  |

## Author

**Moniish Mohansrinivasan**  
**Roll No:** 24BCE5301