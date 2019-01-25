# 1. break
import math

for n in range(99, 0, -1):
    root = math.sqrt(n)
    print('n = {}, root = {}'.format(n, root))
    if root == int(root):
        print(n)
        break


# 2. continue
