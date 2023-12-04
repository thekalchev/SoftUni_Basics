n = int(input())
left_size = 0
right_size = 0
for i in range(2 * n):
    current_num = int(input())
    if i < n:
        left_size += current_num
    else:
        right_size += current_num
if left_size == right_size:
    print(f'Yes, sum = {left_size}')
else:
    print(f'No, diff = {abs(left_size - right_size)}')
