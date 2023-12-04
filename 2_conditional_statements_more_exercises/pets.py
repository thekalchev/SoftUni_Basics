import math

days_away = int(input())
food_left = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())
animal_food = dog_food * days_away + cat_food * days_away + turtle_food * days_away / 1000

if food_left >= animal_food:
    print(f"{math.floor(food_left - animal_food)} kilos of food left.")
else:
    print(f"{math.ceil(animal_food - food_left)} more kilos of food are needed.")
