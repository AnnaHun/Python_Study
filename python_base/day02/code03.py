price = float(input("请输入商品单价"))
amount = int(input("请输入商品数量"))
money = float(input("请输入金额"))
result = money - price * amount
print("应找回"+result)