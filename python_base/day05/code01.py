import copy
list01 = [1,2]
list02 = list01.copy()
list01[0] = 100
print(list02[0])

list03 = [1,[2,3]]
list04 = list03.copy()
list05 = copy.deepcopy(list03)
print(list04)
list04[1][0] = 200
print(list04[1][0])
print(list04)