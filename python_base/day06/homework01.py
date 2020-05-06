list_student_info = []
for i in range(5):
    dict_student = {}
    dict_student["name"] = input("请输入姓名:")
    dict_student["age"] = int(input("请输入年龄:"))
    dict_student["sex"] = input("请输入性别:")

    list_student_info.append(dict_student)

for item in list_student_info:
    for key,value in item.items():
        print("%s----%s"%(key,value))