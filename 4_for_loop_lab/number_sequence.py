import sys

count = int(input())
max_num = - sys.maxsize
min_num = sys.maxsize
for i in range(count):
    num = int(input())
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')