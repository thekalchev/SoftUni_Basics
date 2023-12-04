months = int(input())
water = 20
internet = 15
electricity_total = 0
for month in range(months):
    electricity = float(input())
    electricity_total += electricity

water_total = water * months
internet_total = internet * months
other = (water_total + internet_total + electricity_total) + (water_total + internet_total + electricity_total) * .2
average = (water_total + internet_total + electricity_total + other) / months
print(f'Electricity: {electricity_total:.2f} lv')
print(f'Water: {water_total:.2f} lv')
print(f'Internet: {internet_total:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')
