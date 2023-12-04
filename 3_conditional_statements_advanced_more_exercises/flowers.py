chrysanthemum_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()  # Sprint,Summer,Autumn,Winter
holiday = input()  # Y/N
chrysanthemum_price = 0
roses_price = 0
tulips_price = 0
arrangement_price = 2

if season == "Summer" or season == 'Spring':
    if holiday == 'N':
        chrysanthemum_price = 2
        roses_price = 4.1
        tulips_price = 2.5
    elif holiday == 'Y':
        chrysanthemum_price = 2 * 1.15
        roses_price = 4.1 * 1.15
        tulips_price = 2.5 * 1.15

elif season == 'Winter' or season == 'Autumn':
    if holiday == 'N':
        chrysanthemum_price = 3.75
        roses_price = 4.5
        tulips_price = 4.15
    elif holiday == 'Y':
        chrysanthemum_price = 3.75 * 1.15
        roses_price = 4.5 * 1.15
        tulips_price = 4.15 * 1.15

boquet_price = chrysanthemum_price * chrysanthemum_count + roses_price * roses_count + tulips_price * tulips_count
flower_count = tulips_count + roses_count + chrysanthemum_count

if tulips_count > 7 and season == 'Spring':
    boquet_price = boquet_price - boquet_price * .05

if roses_count >= 10 and season == 'Winter':
    boquet_price *= .9

if flower_count > 20:
    boquet_price *= .8

boquet_price += arrangement_price
print(f'{boquet_price:.2f}')
