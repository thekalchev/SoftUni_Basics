flower_type = input()
count_flowers = int(input())
budget = int(input())
price = 0
discount = 0

if flower_type == 'Roses':
    if count_flowers > 80:
        price = 5 * count_flowers * .9
    else:
        price = 5 * count_flowers

elif flower_type == 'Dahlias':
    if count_flowers > 90:
        price = 3.80 * count_flowers * .85
    else:
        price = 3.8 * count_flowers

elif flower_type == 'Tulips':
    if count_flowers > 80:
        price = 2.8 * count_flowers * .85
    else:
        price = 2.8 * count_flowers

elif flower_type == 'Narcissus':
    if count_flowers < 120:
        price = 3 * count_flowers * 1.15
    else:
        price = 3 * count_flowers

elif flower_type == 'Gladiolus':
    if count_flowers < 80:
        price = 2.5 * count_flowers * 1.2
    else:
        price = 2.5 * count_flowers
leftover = budget - price
needed = price - budget

if budget >= price:
    print(f'Hey, you have a great garden with {count_flowers} {flower_type} and '
          f'{leftover:.2f} leva left.')
else:
    print(f"Not enough money, you need {needed:.2f} leva more.")
