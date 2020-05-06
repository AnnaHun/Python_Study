
year = int(input("请输入年份："))
month = int(input("请输入月份"))
RunNian = bool(year % 4 and year % 100 or year % 400 == 0)
#True是闰年，false是平年
day = None
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    day = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    day = 30
else:
    day = 29 if RunNian else 28
print(str(year)+"年"+str(month)+"月有"+str(day)+"天")
