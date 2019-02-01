# 判断对象是否可以调用
import math

x = 1
y = math.sqrt

print("callable(x) :", callable(x))
print("callable(y) :", callable(y))


# 自定义函数
def hello(name):
    return 'Hello, '+name+"!"

print(hello('Python'))

