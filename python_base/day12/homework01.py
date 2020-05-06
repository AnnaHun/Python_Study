class Weapon:
    def __init__(self,atk):
        self.atk=atk
    def buy(self):
        print("购买武器")
    def attack(self):
        raise NotImplementedError()

class Gun(Weapon):
    def __init__(self,atk,speed):
        super().__init__(atk)
        self.atk_speed=speed
    def attack(self):
        print("开枪啦")

class Grenade(Weapon):
    def __init__(self,atk,range):
        super().__init__(atk)
        self.explode_range=range
    def attack(self):
        print("爆炸啦")


g01=Gun(10,0.1)
g01.buy()
g01.attack()

grenade01=Grenade(50,10)
grenade01.buy()
grenade01.attack()
