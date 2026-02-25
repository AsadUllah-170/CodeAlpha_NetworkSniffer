from scapy.all import sniff, IP, TCP, UDP, ICMP
import csv
from datetime import datetime

packet_count = 0
csv_file = "captured_packets.csv"

# Prepare CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Packet #", "Timestamp", "Source IP", "Destination IP", "Protocol", "Payload (first 50 bytes)"])

def packet_callback(packet):
    global packet_count
    packet_count += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst
        
        if packet.haslayer(TCP):
            proto = "TCP"
            color = "\033[94m"  # Blue
        elif packet.haslayer(UDP):
            proto = "UDP"
            color = "\033[92m"  # Green
        elif packet.haslayer(ICMP):
            proto = "ICMP"
            color = "\033[93m"  # Yellow
        else:
            proto = str(ip_layer.proto)
            color = "\033[0m"   # Default
        
        payload = bytes(packet.payload)
        payload_display = payload[:50] + (b"..." if len(payload) > 50 else b"")
        
        # Print colored output
        print(f"{color}\n===== Packet #{packet_count} =====")
        print(f"Timestamp      : {timestamp}")
        print(f"Source IP      : {src}")
        print(f"Destination IP : {dst}")
        print(f"Protocol       : {proto}")
        print(f"Payload (first 50 bytes): {payload_display}")
        print("=============================\033[0m")
        
        # Save to CSV
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([packet_count, timestamp, src, dst, proto, payload_display])

print("Starting professional network sniffer... (sudo required)")
sniff(prn=packet_callback, count=20)  # Change count=None for continuous capture