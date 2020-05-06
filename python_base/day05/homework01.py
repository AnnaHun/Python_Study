ticket = []
while len(ticket) < 6:
    number = int(input("输入第%d个红球号码"%(len(ticket) + 1)))
    if number <= 0 or number > 33:
        print("不在范围内")
    elif number in ticket:
        print("该号码已经存在")
    else:
        ticket.append(number)

while True:
    number = int(input("请输入篮球号码"))
    if 1 <= number <=16:
        ticket.append(number)
        break
    else:
        print("不在范围内")

for item in ticket:
    print(item)
