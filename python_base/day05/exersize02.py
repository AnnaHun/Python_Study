str_input = "abcdefadfrg"
result = {}
for item in str_input:
    if item not in result:
        result[item] = 1
    else:
        result[item] += 1

print(result)

for item in result.items():
    print(item)