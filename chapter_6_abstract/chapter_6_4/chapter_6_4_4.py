def print_params(*params):
    print(params)


print_params('Testing')
# 输出: ('Testing',)
# 打印了一个元组, 因为里面有个','逗号.
print_params('Test1', '2')