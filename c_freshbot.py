import os
from ftplib import *
import sys
import socket
import time

host = "127.0.0.1"	# Connect home
port = 443

target   = "127.0.0.1"
ftp_port = 21


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

def ftp_port_check():
    try:
        connect = s2.connect((target,ftp_port))
    except:
        print "port 21 closed"
        s.send("s_closed")
        sys.exit()
    print "port 21 open"

while True:
    time.sleep(1)
    srv_cmd = s.recv(1024)
    if srv_cmd == "9j3b3k8":
        ftp_port_check()
        srv_cmd = ""
        s.send("[+] Port 21 open!\n")
        s.send("s_open")


        break
