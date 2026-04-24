from pox.lib.packet.arp import arp
from pox.lib.packet.ipv4 import ipv4
from pox.lib.packet.ipv6 import ipv6

def classify_packet(pkt):
    arp_pkt = pkt.find(arp)
    ipv4_pkt = pkt.find(ipv4)
    ipv6_pkt = pkt.find(ipv6)

    if arp_pkt:
        return "ARP Traffic"
    elif ipv4_pkt:
        return "IPv4 Traffic"
    elif ipv6_pkt:
        return "IPv6 Traffic"
    else:
        return "Unknown Traffic"