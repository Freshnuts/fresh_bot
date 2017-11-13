# freshBot
Small Demonstration of a botnet in Python<br>
<br>
<br>
This botnet will:

1. Target opens c_fresbot.py. Reverse connection is made to C&C.<br>
2. Target receives OK from C&C to start scan.<br>
3. Target scans virtual network for telnet services on other hosts.<br>
<h3>If TRUE;</h3><br>

4. then attack the new system with a dictionary attack.<br>
5. On Success, exfiltrate data from "/etc/passwd".<br>
6. Connect to C&C and send information.<br>
7 Exit.<br>
<br>
<br>
<h3>IF False:</h3><br>
4. Communicate task completed as FAIL with C&C.<br>
5. Exit<br>
