class EmployeeManager:
    """
    员工管理器
    """


    def __init__(self):
        self.__all_employee = []

    # def __str__(self):
    #     return "我的编号是：%d，姓名是：%s，年龄是：%d，成绩是：%d"%(self.id)
    # def __repr__(self):
    #     return ....

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            return
        self.__all_employee.append(employee)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__all_employee:
            total_salary += item.get_salary()
        return total_salary


class Employee:
    """
    员工类
    作用：代表具体员工，隔离员工管理器与具体员工的变化
    """

    def __init__(self, name, salary):
        self.name = name
        self.base_salary = salary

    def get_salary(self):
        return self.base_salary


class Programmer(Employee):
    """
    程序员
    """

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self, value):
        # 扩展重写
        return super().get_salary() + self.bonus


class Salesmen(Employee):
    """
    销售员
    """

    def __init__(self, name, salary, sale_value):
        super().__init__(name, salary)
        self.sale_value = sale_value

    def get_salary(self):
        return super().get_salary() + self.sale_value


manager = EmployeeManager()
manager.add_employee(Employee("zs", 3000))
manager.add_employee(Programmer("xp", 4000, 10))
manager.add_employee(Programmer("xx", 99999, 9876783))
manager.add_employee(Salesmen("pp", 3000, 500))

re = manager.get_total_salary()
print(re)
