moves = int(input())
score = 0
first = 0
second = 0
third = 0
fourth = 0
fifth = 0
invalid_nums = 0
end_score = 0
for move in range(moves):
    points = int(input())
    if 0 <= points <= 50:
        end_score += points

    if 0 <= points <= 9:
        first += 1
        score += points * .2
    elif 10 <= points <= 19:
        second += 1
        score += points * .3
    elif 20 <= points <= 29:
        third += 1
        score += points * .4
    elif 30 <= points <= 39:
        fourth += 1
        score += 50
    elif 40 <= points <= 50:
        fifth += 1
        score += 100
    else:
        invalid_nums += 1
        score /= 2

first_per = first / moves * 100
second_per = second / moves * 100
third_per = third / moves * 100
fourth_per = fourth / moves * 100
fifth_per = fifth / moves * 100
invalid_nums_per = invalid_nums / moves * 100

print(f'{score:.2f}')
print(f'From 0 to 9: {first_per:.2f}%')
print(f'From 10 to 19: {second_per:.2f}%')
print(f'From 20 to 29: {third_per:.2f}%')
print(f'From 30 to 39: {fourth_per:.2f}%')
print(f'From 40 to 50: {fifth_per:.2f}%')
print(f'Invalid numbers: {invalid_nums_per:.2f}%')
