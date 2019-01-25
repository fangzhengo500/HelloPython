d = {
    'x': 1,
    'y': 2,
    'z': 3
}

print(d.items())
for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print('key =', key, ', value =', value)
