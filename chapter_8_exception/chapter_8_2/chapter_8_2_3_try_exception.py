try:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    print(a / b)
except ZeroDivisionError:
    print('The second number can\'t be zero!')
except ValueError:
    print('Input can only be integer')

