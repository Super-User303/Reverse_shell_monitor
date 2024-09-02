# test_network_scanner.py
import unittest
from network_scanner import scan_network

class TestNetworkScanner(unittest.TestCase):
    def test_scan_network(self):
        ip_range = "192.168.0.1/24"
        devices = scan_network(ip_range)
        self.assertIsInstance(devices, list)

if __name__ == "__main__":
    unittest.main()