"""

"""


def get_elements(list_target, v_pos, v_dir, count):
    result = []
    for i in range(count):
        v_pos.x +=v_dir.x
        v_pos.y +=v_dir.y
        result.append((list_target[v_pos.x][v_pos.y]))
    return result


class Vector2:
    """
    向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 实例方法
    def fun01(self):
        pass

    # 类方法
    @classmethod
    def fun02(cls):
        pass

    # 静态方法：得不到对象地址，也得不到类名
    @staticmethod
    def fun03():
        pass


v01 = Vector2()
v01.fun01()  # 隐式传递对象地址

Vector2.fun02()  # 隐式传递类名

Vector2.fun03()

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]

re01 = get_elements(list01, Vector2(1, 0), Vector2(0, 1), 3)
re02 = get_elements(list01, Vector2(2, 1), Vector2(-1, 0), 3)
print(re01)
print(re02)
