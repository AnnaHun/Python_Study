class Grenade:
    def __init__(self, atk):
        self.atk = atk

    def explode(self, *args):
        """
        手雷
        :param args:
        :return:
        """
        for item in args:
            if not isinstance(item, Damageable):
                print("类型不兼容")
                return
            item.damage(self.atk)


class Damageable:
    """
    可以受伤
    """

    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        # 约束子类必须具有当前方法
        # raise NotImplementedError()
        self.hp -= value


class Player(Damageable):
    def damage(self, value):
        # self.hp -= value
        super().damage(value)
        print("碎屏")


class Enemy(Damageable):
    def damage(self, value):
        # self.hp -= value
        super().damage(value)
        print("播放动画")


g01 = Grenade(10)
p01 = Player(100)
e01 = Enemy(50)

g01.explode(p01, e01)
