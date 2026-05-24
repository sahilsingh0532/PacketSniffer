# PacketSniffer

A simple Python-based Packet Sniffer project built for learning network traffic analysis and packet capturing concepts in Cyber Security.

---

## Features

- Capture live network packets
- Monitor incoming and outgoing traffic
- Flask-based UI support
- Beginner-friendly networking project

---

## Requirements

Make sure you have the following installed:

- Python 3
- pip
- Linux (Recommended: Kali Linux / Parrot OS)
- Root/Sudo privileges

---

## Project Structure

```bash
PacketSniffer/
│── app.py
│── sniffer.py
│── ui.py
│── README.md
│── venv/
```

---

# Steps to Start the Packet Sniffer

## Step 1: Open Two Terminals

Open **two terminal windows** in the same project folder.

---

# Terminal 1 — Start Flask App

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Virtual Environment

### Linux / Kali / Parrot

```bash
source venv/bin/activate
```

## Install Required Packages

```bash
pip install flask
```

## Run Flask App

```bash
sudo python app.py
```

---

# Terminal 2 — Start Packet Sniffer

Run the sniffer script with root privileges:

```bash
sudo python sniffer.py
```

---

## Why Sudo is Required

Packet sniffing requires access to low-level network interfaces, which needs administrator/root permissions.

---

## Technologies Used

- Python
- Flask
- Socket Programming
- Networking Concepts

---

## Educational Purpose

This project was created for educational and ethical learning purposes only.

Do not use this tool on networks without permission.

---

## Author

Sahil Singh