prime_nums = 0
non_prime_nums = 0
command = input()
while command != 'stop':
    current_number = int(command)

    is_prime = True
    if current_number < 0:
        print('Number is negative.')
        command = input()
        continue
    for num in range(2, current_number):
        if current_number % num == 0:
            is_prime = False
            break
    if is_prime:
        prime_nums += current_number
    else:
        non_prime_nums += current_number

    command = input()

print(f'Sum of all prime numbers is: {prime_nums}')
print(f'Sum of all non prime numbers is: {non_prime_nums}')