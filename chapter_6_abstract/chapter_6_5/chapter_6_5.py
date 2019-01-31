x = 1

# vars() 返回不可见的字典
scope = vars()
print(scope['x'])
print()

def foo(x):
   scope = vars()
   print(scope['x'])
   x = 38
   scope = vars()
   print(scope['x'])
   print(x)

foo(10)