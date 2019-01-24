# 序列解包
a = 1, 2, 3
print(a)

x, y, z = a
print(x, y, z)

x, y = y, x
print(x, y, z)

scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
print(scoundrel.popitem())
