# 1. 并行迭代
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

for i in range(len(names)):
    print(names[i], ':', ages[i])

lst = list(zip(names, ages))
d = dict(zip(names, ages))
print(lst)
print(d)
