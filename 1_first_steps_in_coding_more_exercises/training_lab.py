length = float(input())
width = float(input())
# limits = 3 <= width <= length <= 100
w = int(((width * 100) - 100) / 70)
l = int((length * 100) / 120)
spaces = (w * l) - 3
print(int(spaces))
