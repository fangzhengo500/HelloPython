# x = []
# x[42] = 'Foobar'    #IndexError: list assignment index out of range
# print(x)

x = {}
x[42] = 'Foobar'
print(x)

# 一个简单程序
# 将人名用作键的字典。每个人都用一个字典表示，
# 字典包含键'phone' 和 'addr', 他们分别于电话号码和地址相关联
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9012',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3159',
        'addr': 'Baz avenue 90'
    },
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name: ')

# 要查询号码还是地址
request = input('Phone number(p) or address(a) ?')

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people:
    print("{}'s {} is {}".format(name, labels[key], people[name][key]))
else:
    print('Not Found: {} !'.format(name))
