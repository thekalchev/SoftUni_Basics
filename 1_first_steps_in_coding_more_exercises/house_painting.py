# ZELENA 1l za 3.4m2
# CHERVENA 1l za 4.3m2
from math import sqrt

door = 1.2 * 2
window = 1.5 * 1.5

house_height = float(input())
house_width = float(input())
roof_height = float(input())

x_sides_area = (house_height * house_height) * 2 - door
y_sides_area = (house_width * house_height) * 2 - window * 2

roof_front_front = 2 * (house_height * roof_height / 2)
roof_side_side = house_width * house_height * 2

print("{:.2f}".format((x_sides_area + y_sides_area) / 3.4))
print("{:.2f}".format(((roof_front_front + roof_side_side) / 4.3)))
