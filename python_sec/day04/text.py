def fun(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


def fun1(n):
    sum = (1 + n) * n / 2
    return sum


def fun02(l):
    for i in l:
        for j in i:
            print(j, end=" ")
        print()
