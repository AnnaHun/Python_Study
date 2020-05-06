"""
    逻辑运算符       与and   或or  非not
                    假       真   反
    身份运算符
"""
print(True and True)

print(True or False)

print(not bool(100))

# 如果第一个条件不满足，则不考虑第二个条件（短路）
# print(1 < 2 and input("请输入") == "a")

# 身份运算符
num01 = 800
num02 = 900
num03 = num01
print(num01 is num02)