"""
    针对列表的自定义工具
"""


class ListHelper:

    @staticmethod
    def find_all(target, func_condition):
        """
            查找列表中满足条件的所有元素
        :param target: 列表
        :param func_condition: 条件
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值
        :return:
        """
        for item in target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(target, func_condition):
        """
            查找列表中满足条件的第一个元素
        :param target:
        :param func_condition:
        :return:
        """
        for item in target:
            if func_condition(item):
                return item

    @staticmethod
    def select(target, func_condition):
        """
            筛选列表中指定条件的数据
        :param target:
        :param func_condition:
        :return:
        """
        for item in target:
            # yield xxx(item)
            yield func_condition(item)

    @staticmethod
    def sum(target, func_condition):
        """
            计算列表中指定条件的所有元素和
        :param target:
        :param func_condition:
        :return:
        """
        sum_value = 0
        for item in target:
            # sum_value += xxx(item)
            sum_value += func_condition(item)
        return sum_value


    @staticmethod
    def sort(target, func_condition):
        """
        万能排序
        :param target: 需要排序的数据
        :param func_condition: 排序的逻辑
        :return:
        """
        for r in range(len(target) - 1):
            for c in range(r + 1, len(target)):
                if func_condition(target[r], target[c]):
                    target[r], target[c] = target[c], target[r]
