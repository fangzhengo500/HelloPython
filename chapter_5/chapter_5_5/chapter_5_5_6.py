# 循环中的else
import math

for n in range(99, 81, -1):
    root = math.sqrt(n)
    if root == int(root):
        print(n)
        break;
else:   # 仅在没有调用break时才执行else的语句
    print("Didn't find it")

for n in range(99, 80, -1):
    root = math.sqrt(n)
    if root == int(root):
        print(n)
        break;
else:   # 仅在没有调用break时才执行else的语句
    print("Didn't find it")
