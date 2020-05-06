import os

pid = os.fork()

if pid < 0:
    print("errot")
elif pid == 0:
    print("child process", os.getpid())
    os._exit(2)
else:
    # pid, status = os.wait()  # 等待处理僵尸--等待子进程的结束
    pid, status = os.waitpid(-1, os.WNOHANG)  # 非阻塞方法
    print("pid", pid)
    print("status", os.WEXITSTATUS(status))
    while True:
        pass
