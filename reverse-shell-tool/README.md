# Reverse Shell Tool

## Description

This tool allows you to scan a network for devices, upload files to a selected Windows machine, and execute commands remotely.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/reverse-shell-tool.git
    cd reverse-shell-tool
    ```

2. Run the installation script:

    ```bash
    sudo ./install.sh
    ```

## Usage

`TODO`

### Network Scanning

To scan the network for devices:

```bash
python3 /usr/local/bin/reverse-shell-network-scanner

File Transfer

To upload files to a Windows machine:

bash

python3 /usr/local/bin/reverse-shell-file-transfer --ip <target_ip> --username <username> --password <password> --domain <domain>

Reverse Shell

The reverse shell script is included as reverse_shell.py. You can execute it directly on the target Windows machine.
Dependencies

    scapy
    pysmb

Install dependencies using:

bash

pip install scapy pysmb

#License

This tool is for educational purposes and ethical hacking. Use responsibly and legally.

#Author

Gideon Kaiyian
