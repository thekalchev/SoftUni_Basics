budget = float(input())
category = input()
people_count = int(input())

VIP_price = 499.99
Normal_price = 249.99
transportation_cost = 0
money_left = 0
money_needed = 0

if 1 <= people_count <= 4:
    transportation_cost = budget * .75
elif 5 <= people_count <= 9:
    transportation_cost = budget * .60
elif 10 <= people_count <= 24:
    transportation_cost = budget * .50
elif 25 <= people_count <= 49:
    transportation_cost = budget * .40
elif 50 <= people_count:
    transportation_cost = budget * .25

group_tickets_VIP = VIP_price * people_count
group_tickets_Normal = Normal_price * people_count

VIP_total = group_tickets_VIP + transportation_cost
Normal_total = group_tickets_Normal + transportation_cost

if category == 'VIP':
    if budget > VIP_total:
        money_left = budget - VIP_total
        print(f'Yes! You have {money_left:.2f} leva left.')
    elif budget < VIP_total:
        money_needed = VIP_total - budget
        print(f'Not enough money! You need {money_needed:.2f} leva.')

if category == 'Normal':
    if budget > Normal_total:
        money_left = budget - Normal_total
        print(f'Yes! You have {money_left:.2f} leva left.')
    elif budget < Normal_total:
        money_needed = Normal_total - budget
        print(f'Not enough money! You need {money_needed:.2f} leva.')
