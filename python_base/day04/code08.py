"""
列表
"""

# 创建空列表
list01 = []
list01 = list()

# 创建具有默认值的列表
list02 = [1,True,1.2]
list02 = list()
list02 = list(range(5))
print(list02)


# 添加元素
list02.append("q")
list02.append("t")
print(list02)

list03 = list("abcd")
print(list03)

list03.insert(2,"bala")
print(list03)

list04 = list("zhuzhaoming")
# 删除指定元素
list04.remove("z")
# 删除指定索引的元素
del list04[1]
print(list04)

# 获取元素
print(list04[:4])

list05 = list("abcdefg")
# 通过切片定位元素
list05[:3] = ["a","b","c","d","e","f"]
print(list05)

# 遍历元素
# for item in range(len(list05)):
#     print(list05[item])
#
#
# print("_________________________________")
#
#
# for item in range(0,len(list05),2):
#     print(list05[item])
#
#
# print("_________________________________")


for item in range(len(list05) -1 ,-1,-1):
    print(list05[item])