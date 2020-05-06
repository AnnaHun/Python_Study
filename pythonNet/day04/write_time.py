import time

f = open('time.txt', 'a+')

f.seek(0)  # 文件偏移量移动到开头

n = 1
for line in f:
    n += 1

while True:
    time.sleep(1)
    s = "%d.    %s\n" % (n, time.ctime())
    f.write(s)
    f.flush()
    n += 1
