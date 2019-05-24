# freshBot
This is a loose Demonstration of a botnet in Python.<br>
The objective of this exercise is to demonstrate a light simulation of the<br>
functions of a botnet. During this project I was able to familiarize myself<br>
with Networking Programming (socket), API communications, ftplib, and<br>
file transfers. The project will take place between a C&C<br>
(Command & Control) Server, and 4 different VM clients on the same virtual<br>
network. This botnet will have the functions of a 'worm', a self<br>
replicating malware that doesn't require a human to propagate.
<br>
<br>
This botnet will:

1. Target opens c_fresbot.py. Reverse connection is made to C&C.<br>

<h3>If TRUE;</h3><br>

2. C&C sends command to begin data exfiltration & file transfer.<br>
3. On success, Target exfiltrates data from "/etc/passwd"<br>
   and sends data to C&C.<br>
4. C&C receives data, then sends 'x' file to target via ftp.
5. Client downloads and & executes file 'x'. (no cleanup for demo)
6. Target scans network for ftp services on other hosts.<br>
7. Taret uploads 'x' file to other hosts with ftp services on network.
8. Target #2 communicates with C&C to exfiltrate data & file transfer.<br>
9. Exit/Disconnect<br>
<br>
<br>
<h3>IF False:</h3><br>
10. Communicate TASK FAILED with C&C & disconnect.<br>
11. Exit<br>
