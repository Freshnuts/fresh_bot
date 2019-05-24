# freshBot
Small Demonstration of a botnet in Python<br>
<br>
<br>
This botnet will:

1. Target opens c_fresbot.py. Reverse connection is made to C&C.<br>
2. Target receives OK from C&C to start network scan.<br>
3. Target scans network for ftp services on other hosts.<br>
<h3>If TRUE;</h3><br>

4. C&C sends command to begin data exfiltration & file transfer.<br>
5. On success, Target exfiltrates data from "/etc/passwd"<br>
   and sends data to C&C.<br>
6. C&C sends 'x' file to target via ftp.
7. Client downloads and & executes file 'x'. (no cleanup for demo)
8. Exit/Disconnect<br>
<br>
<br>
<h3>IF False:</h3><br>
9. Communicate TASK FAILED with C&C & disconnect.<br>
10. Exit<br>
