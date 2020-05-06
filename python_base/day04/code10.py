list01 = [1,2,4,5,8,7,10,33,56,86,100]

max = list01[0]

for i in range(1,len(list01)):
    if max < list01[i]:
        max = list01[i]

print(max)


min = list01[0]

for i in range(1,len(list01)):
    if min > list01[i]:
        min = list01[i]
print(min)