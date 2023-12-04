num_count = int(input())
percent_below_200 = 0
percent_200_399 = 0
percent_400_599 = 0
percent_600_799 = 0
percent_above_800 = 0
for nums in range(num_count):
    number = int(input())
    if 200 > number:
        percent_below_200 += 1
    elif 200 <= number <= 399:
        percent_200_399 += 1
    elif 400 <= number <= 599:
        percent_400_599 += 1
    elif 600 <= number <= 799:
        percent_600_799 += 1
    elif 800 <= number:
        percent_above_800 += 1

total = percent_below_200 + percent_200_399 +percent_400_599 + percent_600_799 + percent_above_800
below_200 = percent_below_200 / total * 100
p_200_399 = percent_200_399 / total * 100
p_400_599 = percent_400_599 / total * 100
p_600_799 = percent_600_799 / total * 100
p_ab_800 = percent_above_800 / total * 100

print(f'{below_200:.2f}%')
print(f'{p_200_399:.2f}%')
print(f'{p_400_599:.2f}%')
print(f'{p_600_799:.2f}%')
print(f'{p_ab_800:.2f}%')
