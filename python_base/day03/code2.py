while True:
    str_usd = input("set dollers")
    float_usd = float(str_usd)
    rmb = float_usd * 6.708
    print(rmb)
    if input("press e to exit") == "e":
        break
