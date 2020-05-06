"""
字符串与列表
"""
# 根据某些逻辑，拼接字符串
list_result = []
for item in range(10):
    # 不用每次拼接都生成一个列表
    list_result.append(str(item))
# 将列表使用链接符，合成一个字符
str_result = "-".join(list_result)
print(str_result)

str_split = str_result.split("-")
print(str_split)
