def find_demo04(target, func_condition):
    for item in target:
        if func_condition():
            yield item


def condition01(item):
    return item.cd == 0


def condition02(item):
    return item.atk > 5


def condition03(item):
    return item.atk > 10 and item.costSP == 0


list_skills = []
for item in find_demo04(list_skills, lambda item: item.cd == 0):
    print(item)


class MyGenerator:
    def __init__(self, target):
        self.target = target
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.target) - 1:
            raise StopIteration
        item = self.target[self.index]
        self.index += 1

        return item
