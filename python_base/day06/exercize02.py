list01 = ["曹操","刘备","孙权"]
list02 = ["曹操","刘备","张飞","关羽"]
set01 = frozenset(list01)
set02 = frozenset(list02)

print(set01 & set02)
print(set01 - set02)
print(set02 - set01)
print("张飞" in set01)
print(set01 ^ set02)
print(len(set01 | set02))