from ftplib import *


ftp = FTP('127.0.0.1')
#ftp.connect([ip], port)
ftp.login(user = 'anonymous', passwd = 'anonymous')
ftp.retrlines('LIST')
fpt.dir()
ftp.quit()

