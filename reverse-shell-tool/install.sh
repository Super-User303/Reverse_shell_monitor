#!/bin/bash
# install.sh
echo "Installing Reverse Shell Tool..."
cp network_scanner.py /usr/local/bin/reverse-shell-network-scanner
cp file_transfer.py /usr/local/bin/reverse-shell-file-transfer
cp reverse_shell.py /usr/local/bin/reverse-shell
chmod +x /usr/local/bin/reverse-shell-network-scanner
chmod +x /usr/local/bin/reverse-shell-file-transfer
chmod +x /usr/local/bin/reverse-shell
echo "Installation complete."