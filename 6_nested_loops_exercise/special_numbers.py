number = int(input())
for num in range(1_111,10_000): #num holds all nums from 1111 to 10000
    num_as_string = str(num) #converting num to a string so we can use it with enumerate
    is_special = True
    for index,digit in enumerate(num_as_string): #digit holds each of ['1','1','1','1'] as strings
        current_digit = int(digit)
        if current_digit == 0:
            is_special = False
            break
        if number % current_digit != 0:
            is_special = False
            break

    if is_special:
        print(f'{num}', end= ' ')