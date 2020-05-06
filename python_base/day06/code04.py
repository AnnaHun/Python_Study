
for r in range(3):
    for c in range(5):
        print("*",end = "")
    print()

print("-----------------------------")
for r in range(4):
    for c in range(6):
        if r % 2 == 0 :
            print("*",end = "")
        else:
            print("#",end = "")
    print()

print("-----------------------------")
for i in range(5):
    for c in range(i+1):
        print("*",end="")
    print()

print("-----------------------------")
for r in range(4):
    for c in range(r):
        print(" ",end="")
    for c in range(4 - r):
        print("#",end="")
    print()

print("-----------------------------")
state = False   #假设没有相同元素
list01 = [1,4,5,7,4,8,0,6]
# 取出前几个元素
for r in range(len(list01) - 1):
    # 与后面元素进行比较
    for c in range(r + 1,len(list01)):
        if list01[r] == list01[c]:
            state = True
            break
    if state:
        break
if state:
    print("具有相同元素")
else:
    print("没有相同元素")



# 取出前几个元素
for r in range(len(list01) - 1):
    # 与后面元素进行比较
    for c in range(r + 1,len(list01)):
        if list01[r] < list01[c]:
            # 交换
            list01[r],list01[c] = list01[c],list01[r]

print(list01)