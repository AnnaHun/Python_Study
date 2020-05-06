# 文件操作示例
# fd = open("test")

try:
    fd = open("test")
except FileNotFoundError as e:
    print(e)
else:
    print("success")

fd.close()