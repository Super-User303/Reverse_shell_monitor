# example_scan.py
from network_scanner import scan_network

def main():
    ip_range = "192.168.0.1/24"
    devices = scan_network(ip_range)
    for device in devices:
        print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}")

if __name__ == "__main__":
    main()