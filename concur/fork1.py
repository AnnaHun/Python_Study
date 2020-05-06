import os
from time import sleep

print("========================")

a = 1

pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    print("child process")
    print("a = %d" % a)
    a=10000
else:
    sleep(1)
    print("parent process")
