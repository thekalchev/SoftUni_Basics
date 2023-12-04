budget_for_group = int(input())
season = input()
fishers_count = int(input())
rent_ship = 0
if season == 'Spring':
    if fishers_count <= 6:
        rent_ship = 3000 * .9
    elif 7 <= fishers_count <= 11:
        rent_ship = 3000 * .85
    else:
        rent_ship = 3000 * .75


elif season == 'Summer' or season == 'Autumn':
    if fishers_count <= 6:
        rent_ship = 4200 * .9
    elif 7 <= fishers_count <= 11:
        rent_ship = 4200 * .85
    else:
        rent_ship = 4200 * .75

elif season == 'Winter':
    if fishers_count <= 6:
        rent_ship = 2600 * .9
    elif 7 <= fishers_count <= 11:
        rent_ship = 2600 * .85
    else:
        rent_ship = 2600 * .75

if fishers_count % 2 == 0 and season != 'Autumn':
    rent_ship = rent_ship * .95

leftover = budget_for_group - rent_ship
needed = rent_ship - budget_for_group

if budget_for_group >= rent_ship:
    print(f'Yes! You have {leftover:.2f} leva left.')
elif budget_for_group < rent_ship:
    print(f'Not enough money! You need {needed:.2f} leva.')
