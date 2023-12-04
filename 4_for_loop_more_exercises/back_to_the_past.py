inherited_cash = float(input())
year_to_live_by = int(input())
money_spent = 0
age = 18
for i in range(1800, year_to_live_by + 1):
    if i % 2 == 0:
        money_spent += 12000
        age += 1
    else:

        money_spent += 12000 + 50 * age
        age += 1

leftover = inherited_cash - money_spent
if money_spent <= inherited_cash:
    print(f'Yes! He will live a carefree life and will have {leftover:.2f} dollars left.')
else:
    print(f'He will need {abs(leftover):.2f} dollars to survive.')