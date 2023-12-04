n1 = int(input())
n2 = int(input())
operator = input()
result = 0
even_or_odd = ''
if operator == '+':
    result = n1 + n2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {even_or_odd}')

elif operator == '-':
    result = n1 - n2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{n1:.0f} {operator} {n2:.0f} = {result} - {even_or_odd}')


elif operator == '*':
    result = n1 * n2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{n1:.0f} {operator} {n2:.0f} = {result} - {even_or_odd}')

elif operator == '/':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 / n2
        print(f'{n1:.0f} {operator} {n2:.0f} = {result:.2f}')

elif operator == '%':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 % n2
        print(f'{n1:.0f} {operator} {n2:.0f} = {result}')
