t01 = {"悟空", "八戒", "沙僧", "唐僧"}
iterator = t01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        break
 