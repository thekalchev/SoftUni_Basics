budget = float(input())
count_statisticians = float(input())
price_clothes_per_statistician = float(input())
decor = budget * .1
if count_statisticians > 150:
    price_clothes_per_statistician *= .9
price_clothes_total = count_statisticians * price_clothes_per_statistician
expenses = decor + price_clothes_total
if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {expenses - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - expenses:.2f} leva left.")
