# 1. 第一种
format = 'Hello, %s. %s enough for ya?'
values = ('world', 'Hot')
print(format % values)

# 2. 第二种
from string import Template

tmpl = Template('Hello, $who! $what enough for ya?')
print(tmpl.substitute(who='Mars', what='Dusty'))

# 3. format
print("{}, {} and {}".format('first', 'second', 'third'))
print("{2}, {1} and {0}".format('first', 'second', 'third'))

print("{3} {0} {2} {1} {3} {0}".format('be', 'not', 'or', 'to'))


# 4. 命名字段
from math import pi
print('{name} is approximately {value:.20f}'.format(name='π', value=pi))