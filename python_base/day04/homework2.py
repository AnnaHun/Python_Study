number = int(input("press number:"))
for i in range(2,number):
    if number % i == 0:
        print("not 素数")
        break
else:
    print("素数")
