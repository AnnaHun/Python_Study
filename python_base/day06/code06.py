
# 形式上的参数
def attack(count):
    """
    套路出拳
    :param count:
    :return:
    """
    for i in range(count):
        print("zuogouquan")
        print("yougouquan")
        print("zhiquan")

def print_rect(r_count,c_count,char):
    """

    :param r_count:
    :param c_count:
    :param char:
    :return:
    """
    for r in range(r_count):
        for c in range(c_count):
            print(char,end="")
        print()

attack(4)

print_rect(3,5,"#")

def print_triangle(height,char):
    for r in range(height):
        for c in range (r+1):
            print(char, end="")
        print()

print_triangle(8,"？")