# A simple calculator

repeat = 'y'
while repeat == 'y' or repeat == 'Y':
    
    num1 = float(input('Enter Num1: '))
    num2 = float(input('Enter Num2: '))

    operation = input('Select +, -, *, /: ')

    if operation == '+':
        print(str(num1) + ' + ' + str(num2) + ' =', num1 + num2)
    elif operation == '-':
        print(str(num1) + ' - ' + str(num2) + ' =', num1 - num2)
    elif operation == '*':
        print(str(num1) + ' * ' + str(num2) + ' =', num1 * num2)
    elif operation == '/':
        print(str(num1) + ' / ' + str(num2) + ' =', num1 / num2)
    else:
        print('ERROR! Wrong Selection.')
    repeat = input('Repeat calculation? [y/n]')

print('Program Ended.')


