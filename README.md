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
This botnet will:

1. drop-master.py will scan network for ssh servers with weak passwords.<br>
2. Two Stage dropper (drop.py) infects<br>
3. drop.py downloads evil_file from evil web server then executes.<br>
4. evil_file connects back to c&c.
5. drop.py = auto-delete/cleans up
