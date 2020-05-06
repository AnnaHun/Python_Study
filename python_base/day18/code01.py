def verify_permissions(func):
    def wrapper(*args,**kwargs):
        print("验证权限")
        return func(*args,**kwargs)
    return wrapper
@verify_permissions
def enter_background(loginId, pwd):
    print(loginId, pwd)
    print("进入后台程序")

@verify_permissions
def delet_order(order_id):
    print("删除%d订单。。。。" % order_id)



enter_background("zs",123)
delet_order(101)