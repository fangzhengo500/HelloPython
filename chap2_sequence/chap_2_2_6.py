# 长度、最大值、最小值
numbers = [100, 34, 678]
print(len(numbers))
print(min(numbers))
print(max(numbers))

arrs = ['ios', 'android', 1, -1, 100]
print(len(arrs))
# print(min(arrs))  #TypeError: '<' not supported between instances of 'int' and 'str'
# print(max(arrs))  #TypeError: '<' not supported between instances of 'int' and 'str'

# account 校验
database = [
    ['admin', '123456'],
    ['android', '123'],
    ['ios', '456']
]

username = input('User name: ')
password = input('Password: ')

if [username, password] in database:
    print('Access granted')
else:
    print('User name or password error!')
