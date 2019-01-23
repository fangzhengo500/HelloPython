#  1. append
lst = [1, 2, 3]
lst.append(4)
print(lst)
print()
# 2. copy
lst2 = lst.copy()
print(lst)
print(lst2)
print()

#  3. clear
lst.clear()
print(lst)
print()

# 4. count
str1 = ['to', 'be', 'or', 'not', 'to', 'be']
print(str1.count('to'))

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1))
print(x.count([1, 2]))
print()

# 5. extend
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
print()

# 6. index
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))
# print(knights.index('a')) ValueError: 'a' is not in list
print()

# 7. insert
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 4)
print(numbers)
print()

# 8. pop
x = [1, 2, 3]
print(x.pop(0))
print(x.pop())
print(x)
print()

# 9. remove
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('to')
print(x)
print()

# 10. reverse
x = [1, 2, 3]
x.reverse()
print(x)
print()

# 11. sort
x = [1, 3, -1, 5.1, 5, -100]
x.sort()
print(x)
print()

# 12. 高级排序
x = ['ios', 'android', 'admin']
x.sort()
print(x)
x.sort(key=len)
print(x)
