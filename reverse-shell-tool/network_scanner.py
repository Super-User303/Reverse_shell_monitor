# network_scanner.py
from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    """Scan the network for devices in the given IP range."""
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    ip_range = "192.168.0.1/24"  # Modify this to your network range
    devices = scan_network(ip_range)
    for device in devices:
        print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}")
