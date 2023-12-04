import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

grape_harvest = x * y
wine_production = 0.4 * grape_harvest / 2.5


if wine_production < z:
    shortage = math.floor(z - wine_production)
    print(f"It will be a tough winter! More {shortage} liters wine needed.")
else:
    total_wine = math.floor(wine_production)
    print(f"Good harvest this year! Total wine: {total_wine} liters.")
    left_wine = total_wine - z
    wine_per_worker = math.ceil(left_wine / workers)
    print(f"{left_wine} liters left -> {wine_per_worker} liters per person.")
