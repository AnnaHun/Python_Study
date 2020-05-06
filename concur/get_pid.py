import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("errot")
elif pid == 0:
    sleep(2)
    print("child pid", os.getpid())
    print("get parent id",os.getppid())
else:
    print('parent pid', os.getpid())
    print("get child pid",pid)
