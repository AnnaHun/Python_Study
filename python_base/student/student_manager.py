"""
学生管理系统
"""


class StudentModel:
    """
    学生数据模型类
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
        创建学生对象
        :param id: 变好
        :param name: 姓名
        :param age:年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


class StudentManagerController:
    """
    学生逻辑控制器
    """

    def __init__(self):
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu[:]

    def add_student(self, stu):
        # 生成编号的需求：新编号比上次添加的对象编号多1
        if len(self.__list_stu) > 0:
            id = self.__list_stu[-1].id + 1
        else:
            id = 1
        stu.id = id()
        self.__list_stu.append(stu)


controller = StudentManagerController()
controller.add_student(StudentModel("zs", 18, 85))
for item in controller.list_stu:
    print(item.id, item.name, item.age, item.score)
