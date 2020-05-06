class GraphicManager:
    def __init__(self):
        # 记录所有面积
        self.__graphics = []

    def add_graphic(self,g):
        if not isinstance(g,Graphic):
            return
        self.__graphics.append(g)

    def get_total_area(self):
        """
        计算总面积
        :return:
        """
        total_area = 0
        for item in self.__graphics:
            total_area += item.get_area()
        return total_area


class Graphic:
    """
    图形
    """

    def get_area(self):
        pass


class Circle(Graphic):
    """
    圆形
    """

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * 3.14


class Rectangle(Graphic):
    """
    矩形
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

