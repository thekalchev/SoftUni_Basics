fuel_type = input()
fuel_amount = float(input())
has_card = input()

fuel_price = 0

if fuel_type == "Gasoline":
    fuel_price = 2.22
    if has_card == "Yes":
        fuel_price -= 0.18
elif fuel_type == "Diesel":
    fuel_price = 2.33
    if has_card == "Yes":
        fuel_price -= 0.12
elif fuel_type == "Gas":
    fuel_price = 0.93
    if has_card == "Yes":
        fuel_price -= 0.08

total_price = fuel_amount * fuel_price

if 20 <= fuel_amount <= 25:
    total_price *= 0.92
elif fuel_amount > 25:
    total_price *= 0.9

print(f"{total_price:.2f} lv.")
