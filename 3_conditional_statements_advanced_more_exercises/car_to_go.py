budget = float(input())
season = input()
car_class = ''
type_car = ''
price = 0
if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        type_car = 'Cabrio'
        price = budget * .35
    elif season == 'Winter':
        type_car = 'Jeep'
        price = budget * .65

elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        type_car = 'Cabrio'
        price = budget * .45
    elif season == 'Winter':
        type_car = 'Jeep'
        price = budget * .8

elif budget > 500:
    car_class = 'Luxury class'
    type_car = 'Jeep'
    price = budget * .9

print(f'{car_class}')
print(f'{type_car} - {price:.2f}')
