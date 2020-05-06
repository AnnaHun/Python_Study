"""
    函数返回值
"""


def add(num1, num2):
    result = num1 + num2
    return result


def num_compare(list_target):
    for r in range(len(list_target) - 1):
        # 与后面元素进行比较
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True
    return False


def is_uneven(number):
    return number % 2 == 1


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_day_by_month(year, month):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


def get_min(list_target):
    min = list_target[0]
    for i in range(1, len(list_target)):
        if min > list_target[i]:
            min = list_target[i]
    return min


def get_chinese_char_count(str_target):
    count = 0
    for item in str_target:
        if 0x4E00 <= ord(item) <= 0x9FA5:
            count += 1
    return count


def get_prime(begin, end):
    list_prime = []
    for number in range(begin, end + 1):
        if is_prime(number):
            list_prime.append(number)
    return list_prime


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
