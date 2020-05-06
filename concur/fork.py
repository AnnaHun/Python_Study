import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    sleep(5)
    print("the new process")
else:
    sleep(6)
    print("the old process")
print("fork test over")
