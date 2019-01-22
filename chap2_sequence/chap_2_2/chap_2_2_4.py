# 序列乘法
str = 'python '
print(str * 7)

print([69] * 0)

input_str = input('Please input something: \n')

input_str_len = len(input_str);
margin_len = 4;

print()
print('+' + '-' * (input_str_len + margin_len * 2 - 2) + '+')
print('|' + ' ' * (margin_len - 1) + input_str + ' ' * (margin_len - 1) + '|')
print('+' + (input_str_len + margin_len * 2 - 2) * '-' + '+')
