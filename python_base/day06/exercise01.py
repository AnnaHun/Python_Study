set_target = set()
while True:
    str_input = str(print("请输入"))
    if "e" is str_input:
        break
    set_target.add(str_input)

for item in set_target:
    print(item)