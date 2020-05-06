def print_func_name(func):
    def wrapper():
        print(func.__name__)
        func()

    return wrapper()

@print_func_name
def say_hello():
    # print_func_name(say_hello())
    print("hello")

@print_func_name
def say_goodbye():
    # print_func_name(say_goodbye())
    print("goodbye")



say_hello()
say_goodbye()
