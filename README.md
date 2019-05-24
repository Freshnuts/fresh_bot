# freshBot
Small Demonstration of a botnet in Python<br>
<br>
<br>
This botnet will:

1. Target opens c_fresbot.py. Reverse connection is made to C&C.<br>
2. Target receives OK from C&C to start network scan.<br>
3. Target scans network for ftp services on other hosts.<br>
<h3>If TRUE;</h3><br>

4. Host sends commands to for data exfiltration.<br>
5. On Success, exfiltrate data from "/etc/passwd".<br>
6. Connect to C&C and send data.<br>
7. C&C sends 'x' file to target via ftp.
8. Client executes.
7. Exit<br>
<br>
<br>
<h3>IF False:</h3><br>
4. Communicate TASK FAILED with C&C & disconnect.<br>
5. Exit<br>
