# CodeAlpha Network Sniffer - Task 1

## Overview
This Python project is built for the **CodeAlpha Cyber Security Internship (Task 1: Network Sniffer)**.  
It captures live network packets passing through your machine and provides detailed information about each packet.  

With this tool, you can:  
- Monitor network traffic in real-time.  
- View source and destination IP addresses.  
- Identify the protocol (TCP, UDP, ICMP).  
- Inspect the first 50 bytes of the packet payload.  
- Save captured data into a CSV file for analysis.  

> ⚠️ Note: To capture packets on Linux, this script needs to be run with `sudo` due to raw socket permissions.

---

## Features
- Real-time packet capture using **Scapy**.  
- Automatic **CSV file generation** (`captured_packets.csv`) with all packet details.  
- Simple terminal output with packet number, timestamp, IP addresses, protocol, and payload preview.  
- Designed for internship submission: clean, professional, and ready for GitHub.

---

## Requirements
- **Python 3.x**  
- **Scapy library**: Install via pip:  
  ```bash
  pip install scapy

  How to Run

Navigate to the project directory:

cd ~/NetworkSniffer

Activate Python virtual environment:

source venv/bin/activate

Run the sniffer with root permissions:

sudo python sniffer.py

The terminal will display each captured packet in real-time:

Packet #1
Timestamp: 2026-02-25 20:15:32
Source IP: 10.116.116.54
Destination IP: 172.64.155.209
Protocol: TCP
Payload (first 50 bytes): b'E\x00\x00\x34...'

After capturing, open captured_packets.csv for a table view of all packets.
