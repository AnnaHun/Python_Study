def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证")
        return func(*args, **kwargs)

    return wrapper


@verify_permissions
def deposit(money):
    print("存款", money)


@verify_permissions
def withdraw():
    print("取钱")
    return 10000


deposit(5000)
print(withdraw())
