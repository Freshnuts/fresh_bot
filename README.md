# freshBot
This is a loose Demonstration of a botnet in Python.<br>
The objective of this exercise is to demonstrate the functions of a botnet.<br>
<br>
Players in the game<br>
===================<br>
command & control server<br>
evil web server<br>
scanner + drop master<br>
4 VM clients on the same virtual network<br>

<br>
<br>
Functions:
1. drop-master.py will scan network for ssh servers with weak passwords.<br>
   and perform a dictionary attack.
2. drop-master.py performs RCE.<br>
3. RCE downloads evil_file from evil_web_server<br>
4. evil_file connects back to c&c.
5. drop.py = auto-delete/cleans up
