budget = float(input())
season = input()
location = ''
accomodation = ''
price = 0
if budget <= 1000:
    accomodation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * .65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * .45

if 1000 < budget <= 3000:
    accomodation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * .8
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * .6

if budget > 3000:
    accomodation = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * .9
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * .9

print(f'{location} - {accomodation} - {price:.2f}')
