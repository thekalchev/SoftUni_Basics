fuel_type = input()
fuel_level = float(input())

while True:
    if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
        if fuel_level >= 25:
            print(f"You have enough {fuel_type.lower()}.")
        else:
            print(f"Fill your tank with {fuel_type.lower()}!")
        break
    else:
        print("Invalid fuel!")
        break
