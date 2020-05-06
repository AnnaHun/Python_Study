"""
集合
    有一系列不重复的不可变类型变量组成的可变映射容器【类型不可变，但是同类型的还是可以更改滴】
    相当于只有建，没有值的字典
"""

# 创建空集合
s01 = set()

# 创建具有默认值的集合
s01 = {1,2,3,4}
print(type(s01))
# 集合的特点是不重复     --天然的去重


# 其他容器 -->集合
s02 = set("abcdace")
print(s02)

l02 = list(s02)
print(l02)

t02 = tuple(s02)#将集合转换为元组
print(t02)

# 集合是无序的
# 集合的增删改查
s02.add("1")
s02.add("2")
s02.add("3")
print(s02)

if "1" in s02:
    s02.remove("1")

s02.discard("2")#自动判断是否是空方法
print(s02)

# 获取所有元素
for item in s02:
    print(item)

# 计算
s03 = {1,2,3}
s04 = {2,3,4}

# 计算两集合交集
s05 = s03 & s04
print(s05)

# 合集
s06 = s03 | s04
print(s06)

# 补集
s07 = s03 ^ s04
print(s07)

# 子集
s08 = {1,2,3}
s09 = {2,3}
re = s08 <s09
# 返回true说明s09是s08的子集
print(re)

