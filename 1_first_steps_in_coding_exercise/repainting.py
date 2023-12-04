plastic = float(input()) * 1.50
paint = float(input()) * 14.50
distributor = float(input()) * 5.00
hours = int(input())
paint = paint + paint * .10
plastic = plastic + 3
plastic_bags = .40
total = plastic + paint + distributor + plastic_bags
print(total + total * hours * .30)
