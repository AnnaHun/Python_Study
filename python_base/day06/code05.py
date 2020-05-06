"""
    列表推倒式嵌套
"""
list01 = ["a","b","c"]
list02 = ["A","B","C"]
list03 = []
for r in list01:
    for c in list02:
        list03.append(r+c)
print(list03)

list03 = [r+c for r in list01 for c in list02]

list04 = ["香蕉","苹果","哈密瓜"]
list05 = ["可乐","牛奶"]
list06 = [r+c for r in list04 for c in list05]
print(list06)