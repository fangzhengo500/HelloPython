# 函数内部赋值对外部没有任何影响
def try_to_change(n):
    n = 'Try to change'


name = 'Msr. Lee'
try_to_change(name)
print(name)


def change(n):
    n[0] = 'change 1'


names = ['1', '2', '3']
change(names)
print(names)

# 字典查询
me = 'Magnus Lie Hetland'
storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

storage['first']['Magnus'] = me
storage['middle']['Lie'] = me
storage['last']['Hetland'] = me

print(storage)


