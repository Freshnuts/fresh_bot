import paramiko
import time

# ssh process
p = paramiko.SSHClient()

# set policy when host key is unknown
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())

i = 1
# connect to server on port 2222
for i in range(2):
    p.connect('challenge02.root-me.org', port=2222, username='app-systeme-ch13', password='app-systeme-ch13')

# commands -> file descriptors
    stdin, stdout, stderr = p.exec_command('ls')

    for line in stdout:
        print(line.strip('\n'))
    for line in stderr:
        print(line.strip('\n'))
    p.close()
