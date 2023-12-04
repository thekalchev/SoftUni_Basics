x = float(input())
while x >= 0:
    y = x * 2
    print(f'Result: {y:.2f}')
    x = float(input())

else:
    print('Negative number!')
    exit()