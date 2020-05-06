# 1.整数 int
# 十进制
num01 = 18
# 二进制需要在前面加个0b
num02 = 0b11
print(num02)
# 八进制需要在数字前面加0o
num03 = 0o10
print(num03)
# 十六进制需要在前面加上0x
num04 = 0x10
print(num04)

# 小整数对象池
a = 5000
b = 5000
# id函数：返回变量存储的对象地址
print(id(a))
print(id(b))

# 2.浮点数 float
f01 = 1.0
f02 = 1.234e2
f03 = 1.234e-3
print(f02)
print(f03)

# 3。字符串str
s01 = "唐僧"
s02 = "10"
s03 = "1。5"
print("10"+ "2")

# 4.复数 complex  在数字后面加j，加j的为虚部
c01 = 1j
c02 = 5 + 1j
print(c02)
print(type(c01))

# 5。布尔 boor
b01 = True
b02 = False
b03 = 1 > 2
print(b03)


# 6.数据类型转换
# str_score = input("请输入成绩")
# input函数的结果就是str，如果需要做数学运算，必须转换成数字
# print(type(str_score))
# float_score = float(str_score)
# print(type(float_score))

b04 = bool("False")
print(b04)

#如果需要转换的类型，与目标类型不一致，则错误
i01 = int("5+")
print(i01)