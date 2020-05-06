number = int(input("请输入"))
print("*" * number)
for i in range(number - 2):
    print("*" + " " * (number - 2) + "*")

print("*" * number)