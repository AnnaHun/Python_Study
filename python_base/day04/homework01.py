height = 100
count = 0
distance = height
while height / 2 >= 0.01:
    count +=1
    height /= 2
    print("第"+str(count)+"次"+str(height))
    distance += height*2
print(round(distance,2))
