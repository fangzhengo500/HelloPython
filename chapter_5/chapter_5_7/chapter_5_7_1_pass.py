name = input('input a name:\n')

if name in ['Ralph', 'Auldus', 'Melish']:
    print('Welcome!')
elif name == 'Enid':
    # python 代码块不能为 pass,什么都不做
    pass
elif name in ['Bill', 'Gates']:
    print('Hello')
else:
    print('Access Denied')