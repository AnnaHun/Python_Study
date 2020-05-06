class Wife:
    # 计数器
    count = 0
    @classmethod
    def get_count(cls):
        return Wife.count

    def __init__(self, name):
        self.name = name

        Wife.count += 1


w01 = Wife("小乔")
w02 = Wife("大乔")
# 通过雷鸣，访问类方法
print(Wife.get_count())

