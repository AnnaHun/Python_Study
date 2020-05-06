month = int(input("请输入月份"))
if month < 1 or month >12:
    print("输入有误")
else:
    # 将每月的天数，存入元组
    day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
    print(day_of_month[month - 1])


# 累加
result = sum(day_of_month[:month - 1])