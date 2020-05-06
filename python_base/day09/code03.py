"""
使用属性封装变量
"""


class Wife:
    def __init__(self,name,age):

        self.name = name

        self.age=age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
