# 1. 简单切片
url = 'http://www.python.com'
domain = url[11:-4]

print('Domain name: ' + domain)

# 2. 步长切片
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::-1])
print(numbers[0:10:3])
print(numbers[::4])

