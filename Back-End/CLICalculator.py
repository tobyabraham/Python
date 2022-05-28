def calc():
    operator = input('''
Please select the operator you would like to use by typing in any of the math operators available:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    value_1 = int(input("Enter first number: "))
    value_2 = int(input("Enter second number: "))

    if operator == '+':
        print('{} + {} = '.format(value_1, value_2))
        print(value_1 + value_2)

    elif operator == '-':
        print('{} - {} = '.format(value_1, value_2))
        print(value_1 - value_2)

    elif operator == '*':
        print('{} * {} = '.format(value_1, value_2))
        print(value_1 * value_2)

    elif operator == '/':
        print('{} / {} = '.format(value_1, value_2))
        print(value_1 / value_2)

    else:
        print('You have not selected a valid operator, please run the program again.')

calc()