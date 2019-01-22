# 1. 修改列表:
x = [1, 1, 1]
x[1] = 0;
print(x)
print()

# 2. 删除元素
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[0]
print(names)
print()

# 3.切片赋值
name = list('Perl')
print(name)
name[1:] = list('ython')
print(name)
print()

# 3.切片赋值 - 插入
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)
print()

# 3.切片赋值 - 删除
numbers[1:4] = []
print(numbers)
print()

