import random


randomNum = random.randint(1,100)
count = 0
while count < 10:
    count +=1
    input_number = int(input("the "+str(count)+"times please:"))
    if input_number > randomNum:
        print("big")
    elif input_number <randomNum:
        print("small")
    else:
        print("congratulations")
        break
else:
    print("you are so stupid")