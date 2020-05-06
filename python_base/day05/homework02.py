import random

ticket = []
while len(ticket) < 6:
    number = random.randint(1,33)
    if number not in ticket:
        ticket.append(number)

# 排序
ticket.sort()

ticket.append(random.randint(1,16))

# 通过切片返回新列表
temp = ticket[:6]
# 对新列表进行排序
temp.sort()
# 更换列表中内容
ticket[:6] = temp

for item in ticket:
    print(item)

print(ticket)