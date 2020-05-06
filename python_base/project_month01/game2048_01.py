"""
    2048核心算法
"""

list01 = [
    [2, 0, 0, 4],
    [4, 2, 2, 4],
    [4, 2, 4, 2],
    [4, 2, 2, 2],
]


def zero_to_end01(list_target):
    """
    元素零的右移
    :param list_target: 传入的列表
    :return:排列好的列表
    """

    # 1.将传入的列表中非零元素，拷贝到新列表中
    new_list = []
    new_list = [item for item in list_target if item != 0]
    # 2.根据为零元素的数量，在新列表中添加零元素
    new_list += [0] * list_target.count(2)
    # 将新列表中的元素赋值给传入的列表
    list_target[:] = new_list


def zero_to_end02(list_target):
    """
     元素零的右移
    :param list_target: 传入的列表
    :return:排列好的列表
    """
    # 从后往前判断如果零元素，则删除。再末尾追加零元素
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)


def merge(llist_target):
    """
    相同相加
    :param llist_target:
    :return:
    """
    zero_to_end01(llist_target)
    for i in range(len(llist_target) - 1):
        # 相邻且相同
        if llist_target[i] == llist_target[i + 1]:
            llist_target[i] += llist_target[i + 1]
            llist_target[i + 1] = 0
    zero_to_end01(llist_target)


def print_map(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c], end=" ")
        print()


def move_left(map):
    for r in range(len(map)):
        # 从左往右获取行
        # 交给merge进行合并
        merge((map[r]))


def move_right(map):
    for r in range(len(map)):
        # 从右往左获取行
        # 交给merge进行合并
        list_merge = map[r][::-1]
        map(list_merge)
        map[r][::-1] = list_merge


def move_up(map):
    for c in range(4):
        list_merge = []
        # 从上往下获取列，形成一维列表
        for r in range(4):
            list_merge.append(map[r][c])
        # 交给合并方法
        merge(list_merge)
        # 将合并后的结果还给原来的二维列表
        for r in range(4):
            map[r][c] = list_merge[r]


def move_down(map):
    for c in range(4):
        list_merge = []
        # 从上往下获取列，形成一维列表(从左到右)
        for r in range(3, -1, -1):
            list_merge.append(map[r][c])
        # 交给合并方法
        merge(list_merge)
        # 将合并后的结果(从左到右)还给原来的二维列表
        for r in range(3, -1, -1):
            map[r][c] = list_merge[3 - r]


move_down(list01)
print_map(list01)
