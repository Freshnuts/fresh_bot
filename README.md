# freshBot
Demonstration of a simple botnet written in Python.<br>
<br>
"scan_drop.py" scans virtual network, if it finds a node with ssh service<br>
running it performs a dictionary attack on it. Once, correct credentials are<br>
provided, 1st payload executes and directs target to download an "evil_file"<br>
from our web server.
<br>
<h1>The Environment Setup<h1><br>
<br>
1. Our Attack machine: **Linux kali 4.16.0-kali2-amd64**<br>
2. Web Server hosting for 2nd Stage payload, "evil_file".<br>
3. 4 x **ubuntu-16.04.5-desktop-amd64** in the same virtual network.<br>
4. Python - paramiko module.
5. msfvenom
6. msf5 > exploit/multi/handler module
7. scan_drop.py - Scans, Dictionary Attack, send 1st stage payload, RCE.

<br>
<br>
Functions:<br>
# scan_drop.py functions<br>
1. scans virtual network for nodes running ssh services on port 22.<br>
2. If service found on node perform dictionary attack.<br>
3. If dictionary attack successful, RCE:<br>
&#160;&#160;a. "wget" "evil_file" our vulnerable servers.<br>
&#160;&#160;b. run payload.<br>
&#160;&#160;c. delete payload & disconnect.<br>
<br>
<br>
# evil_file functions<br>
# 1. "evil_file" is a binary meterpreter tcp reverse shell to C&C.<br>
# 2. C&C takes over while scan_drop.py disconnects.<br>
