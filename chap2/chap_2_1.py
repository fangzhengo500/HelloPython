months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

month = input('请输入需要查询的月份:\n')
month_name = months[int(month) - 1]
print(month_name + ' = ' + month + "月")
