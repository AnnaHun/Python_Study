"""
字典推导式
"""

dic01 = {}
for item in range(1,10):
    dic01[item] = item ** 2

print(dic01)

dic02 = {item:item ** 2 for item in range(1,10) if item % 2 == 0}
print(dic02)