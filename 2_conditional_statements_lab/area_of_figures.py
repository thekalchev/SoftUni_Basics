from math import pi

type = input()
area = 0
if type == "square":
    side = float(input())
    area = side * side

elif type == "circle":
    radius = float(input())
    area = pi * radius ** 2

elif type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

elif type == "triangle":
    side_a = float(input())
    height = float(input())
    area = side_a * height / 2

print(f"{area:.3f}")
