veggies = float(input())
fruit = float(input())
kg_veggies = float(input())
kg_fruit = float(input())
price_veggies = veggies * kg_veggies
price_fruit = fruit * kg_fruit
total = (price_veggies + price_fruit) / 1.94
print("{:.2f}".format(total))
