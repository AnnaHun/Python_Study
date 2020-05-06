# list01 = ["张三丰","张无忌","赵敏"]
# dict01 = {}
# for item in list01:
#     dict01[item] = len(item)
# print(dict01)
#
# dict02 = {item:len(item) for item in list01}
# print(dict02)

list01 = ["张三丰","张无忌","赵敏"]
list02 = [101,102,102]
dict01 = {}
# for i in range(len(list01)):
#     dict01[list01[i]] = list01[i]

dict02 = {list01[i]:list02[i] for i in range(len(list01))}
# print(dict02)
# dict03 = {value:key for key,value in dict02.items()}
# print(dict03)


list03 = [(value,key) for key,value in dict02.items()]
print(list03)
