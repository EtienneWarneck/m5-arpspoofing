from scapy.all import *

arp_response = ARP()
print(arp_response.show())