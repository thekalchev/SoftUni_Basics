season = input()
km_per_month = float(input())
cash_per_km = 0

if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        cash_per_km = .75
    elif season == 'Summer':
        cash_per_km = .9
    elif season == 'Winter':
        cash_per_km = 1.05

if 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        cash_per_km = .95
    elif season == 'Summer':
        cash_per_km = 1.1
    elif season == 'Winter':
        cash_per_km = 1.25

if 10000 < km_per_month <= 20000:
    cash_per_km = 1.45

total_cash = km_per_month * cash_per_km * 4
total_cash_after_tax = total_cash * .9
print(f'{total_cash_after_tax:.2f}')
