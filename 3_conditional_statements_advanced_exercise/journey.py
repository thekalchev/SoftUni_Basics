budget = float(input())
season = input()
destination = ''
accommodation = ''
spend = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        spend = budget * .3
        accommodation = 'Camp'
    elif season == 'winter':
        spend = budget * .7
        accommodation = 'Hotel'

elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        spend = budget * .4
        accommodation = 'Camp'
    elif season == 'winter':
        spend = budget * .8
        accommodation = 'Hotel'

elif budget > 1000:
    destination = 'Europe'
    if season == 'summer':
        spend = budget * .9
        accommodation = 'Hotel'
    elif season == 'winter':
        spend = budget * .9
        accommodation = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{accommodation} - {spend:.2f}')
