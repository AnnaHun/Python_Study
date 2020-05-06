"""
固定集合
"""
f01 = frozenset([1, 2, 3, 3, 2])
print(type(f01))
print(f01)


def sort(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] < list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    return list_target
list01=[1,4,2,19,39,77,29,44,56]
sort(list01)
print(list01)