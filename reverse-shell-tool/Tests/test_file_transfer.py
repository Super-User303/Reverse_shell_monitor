# test_file_transfer.py
import unittest
from file_transfer import upload_files

class TestFileTransfer(unittest.TestCase):
    def test_upload_files(self):
        ip_address = '192.168.0.105'
        username = 'admin'
        password = 'password'
        domain = 'WORKGROUP'
        file_paths = ['reverse_shell.py', 'run_script.bat', 'run_script.vbs']
        try:
            upload_files(ip_address, username, password, domain, file_paths)
            self.assertTrue(True)  # You would include real checks in a full implementation
        except Exception as e:
            self.fail(f"File transfer failed: {e}")

if __name__ == "__main__":
    unittest.main()