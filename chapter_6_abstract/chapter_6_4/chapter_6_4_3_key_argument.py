# 关键字参数, 和默认值
# 注: 通常位置参数和关键字参数不结合使用, 反面教材如下
def hellow(name, greeting='Hello', punctuation='!'):
    print('{},{}{}'.format(greeting, name, punctuation))


hellow('Mars')
hellow('Mars', 'Howdy')
hellow('Mars', 'Howdy', '...')
hellow('Mars', punctuation='.')
hellow()
