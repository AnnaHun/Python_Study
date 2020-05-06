"""
面向对象：考虑问题，从对象的角度出发
类：模板        抽象
对象：具体
"""


class Wife:
    """
    老婆
    """

    # 1.数据成员
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 2.方法成员
    def cooking(self):
        print(self.name+"做饭")


# 创建对象（实例化）
# 调用__init__(self,name,age,sex)方法
w01 = Wife("花花", 26, "女")
w01.cooking()
