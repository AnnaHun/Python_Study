class Student:
    def __init__(self,name,sex,age,score):
        self.name=name
        self.sex=sex
        self.age=age
        self.score=score

    def print_self(self):
        print(self.name,self.sex,self.age,self.score)

list_stu=[
    Student("zs","男",25,86),
    Student("ls","女",25,100),
    Student("ww","男",25,89),
    Student("zl","女",25,95),
]

def get_student_for_name(list_target,name):
    for stu in list_target:
        if stu.name==name:
            return stu

re01=get_student_for_name(list_stu,"ls")
re01.print_self()

def get_students_for_sex(list_target,sex):
    result = []
    for stu in list_target:
        if stu.sex==sex:
            result.append(stu)
    return result

r02=get_students_for_sex(list_stu,"女")
for item in r02:
    item.print_self()
