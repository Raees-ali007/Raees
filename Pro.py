import os
import subprocess as sub
import time
time.sleep(1.5)
sub.run(['pkg', 'update'])
sub.run(['pkg', 'upgrade'])
sub.run(['pkg', 'uninstall', 'python'])
sub.run(['pkg', 'install', 'python'])
os.system('git pull')
os.system('chmod 777 AWAN')
os.system('./AWAN')
