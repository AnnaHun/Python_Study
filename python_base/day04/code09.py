lise_name = list()

while True:
    name = input("请输入第%d个学生的姓名"%(len(lise_name)))
    if name == "esc":
        break
    if name not in lise_name:
        lise_name.append(name)

for item in lise_name:
    print(item)