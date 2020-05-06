"""
字典
"""
d01 = {}
d01 = dict()

d01 = {"a":"A","b":"B"}
# d02 = dict("abcd")#分不清key value
d02 = dict([(1,2),(3,4)])
print(d02)

d01["c"] = "c"
print(d01)
d01["c"] = "C"
print(d01)

# 获取字典中所有记录（元组）
for item in d01.items():
    print(item)

for k,v in d01.items():
    print(k)
    print(v)