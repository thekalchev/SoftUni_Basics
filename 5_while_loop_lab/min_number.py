import sys
number= input()
lowest = sys.maxsize
while number != 'Stop':
    current_number = float(number)
    if current_number < lowest:
        lowest = current_number
    number = input()
print(f'{lowest:.0f}')