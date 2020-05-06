import random

# 胜利策略
wins = (
    ("石头","剪刀"),
    ("剪刀","布"),
    ("布","石头")
)
# 将用户猜的拳与系统出拳形成一个元组
user_input_index = int(input("请输入整数（0表示拳头；1表示剪刀，2表示布）:"))
items = ("石头","剪刀","布")
user_input_item = items[user_input_index]

sys_input_index = random.randint(0,2)
sys_input_item = items[sys_input_index]


if user_input_item == sys_input_item :
    print("平局")
elif (user_input_item,sys_input_item) in wins:
    print("赢了")
else:
    print("输了")