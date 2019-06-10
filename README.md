# freshBot
Demonstration of a botnet in Python.<br>
The objective of this exercise is to get an idea how a botnet works, and<br>
to familiarize myself with Socket, Multiprocessing, and (ssh)paramiko libraries.<br>
<br>
Players in the game<br>
===================<br>
command & control server<br>
evil web server<br>
scan_drop.py<br>
4 VM clients on the same virtual network<br>

<br>
<br>
Functions:<br>
1. scan_drop.py will scan network for ssh servers with weak passwords<br>
&nbsp;&nbsp;&nbsp;and perform a dictionary attack.<br>
2. scan_drop.py performs RCE.<br>
3. RCE downloads evil_file from evil_web_server<br>
4. evil_file connects back to c&c.
