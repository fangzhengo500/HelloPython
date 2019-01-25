scoundrel = {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
robin = scoundrel
print('scoundrel = {}'.format(scoundrel))
print('robin = {}'.format(robin))

scoundrel = None
print('scoundrel = {}'.format(scoundrel))
print('robin = {}'.format(robin))
print()

# del: 会删除引用对象,还会删除名称本身
a = {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
b = a
print('a = {}'.format(a))
print('b = {}'.format(b))
print()

del a
# print('scoundrel = {}'.format(scoundrel)) NameError: name 'scoundrel' is not defined
print('b = {}'.format(b))

# a和b指向同一个列表，但删除x对y没有任何影响，因为你只删除名称a，而没有删除列表本身（值）。
# 事实上，在Python中，根本就没有办法删除值，而且你也不需要这样做，因为对于你不再使用的值，
# Python解释器会立即将其删除。
