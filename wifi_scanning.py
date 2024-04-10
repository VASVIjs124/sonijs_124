import scapy.all as scapy
import re
import socket

ip_add_range_pattern=re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
 ip_add_range_entered=input("\nPlease enter the IP address and range that you want to send the ARP request to (ex 192.168.1.0/24):")
 if ip_add_range_pattern.search(ip_add_range_entered):
  print(f"{ip_add_range_entered} is a valid Ip address range")
  break

# Perform ARPing
arp_result=scapy.arping(ip_add_range_entered, verbose=False)[0]

# Display results with hostnames
for sent, received in arp_result:
 ip=received.psrc
 mac=received.hwsrc
 try:
  socket.gethostbyaddr(ip)
 except socket.herror:
  hostname="Unknown"
 print(f"IP: {ip} MAC: {mac} Hostname:{hostname}")
