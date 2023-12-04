import sys
sum = 0
max_num = -sys.maxsize
num_count = int(input())
for i in range(num_count):
    number = int(input())
    if number > max_num:
        max_num = number
    sum += number
rest_sum = sum - max_num
if max_num == sum/2:
    print(f'Yes\nSum = {max_num}')
else:
    diff = abs(max_num - rest_sum)
    print(f'No\nDiff = {diff}')