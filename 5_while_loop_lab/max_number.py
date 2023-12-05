import sys
number= input()
highest = -sys.maxsize
while number != 'Stop':
    current_number = float(number)
    if current_number > highest:
        highest = current_number
    number = input()
print(f'{highest:.0f}')