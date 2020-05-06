class Enemy:
    def __init__(self, name="", hp=0, atk=0.0, atk_speed=0.0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_speed = atk_speed

    def print_self(self):
        print(self.name, self.hp, self.atk, self.atk_speed)


list_enemy = []
for i in range(3):
    e = Enemy()
    e.name = input("name")
    e.hp = int(input("hp"))
    e.atk = int(input("atk"))
    e.atk_speed = float(input("atk_speed"))
    list_enemy.append(e)

for item in list_enemy:
    item.print_self()


