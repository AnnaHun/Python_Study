str_input = input("please press what you want init")
print(str_input[0])
print(str_input[-len(str_input)])

print(str_input[-1])
print(str_input[len(str_input) - 1])

if len(str_input) %2 == 1:
    print(str_input[len(str_input) // 2])

print(str_input[-3:])

print(str_input[::-1])
