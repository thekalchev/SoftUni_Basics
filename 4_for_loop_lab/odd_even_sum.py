count_of_numbers = int(input())
even_nums = 0
odd_nums = 0
for numbers in range(count_of_numbers):
    current_number = int(input())
    if numbers % 2 == 0:
        even_nums += current_number
    else:
        odd_nums += current_number

if even_nums == odd_nums:
    print('Yes')
    print(f'Sum = {even_nums}')
else:
    print('No')
    print(f'Diff = {abs(even_nums - odd_nums)}')
