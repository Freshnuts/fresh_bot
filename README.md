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
# scan_drop.py functions<br>
# 1. scans virtual network for nodes running ssh services on port 22.<br>
# 2. If service found on node perform dictionary attack.<br>
# 3. If dictionary attack successful, RCE:<br>
#<&#9;>user@target# "wget" a file (evil_file) from our web server.<br>
#<&#9;>user@target# run payload.<br>
#<&#9;>user@target# delete payload & disconnect.<br>
<br>
<br>
# evil_file functions<br>
# 1. "evil_file" is a binary meterpreter tcp reverse shell to C&C.<br>
# 2. C&C takes over while scan_drop.py disconnects.<br>
