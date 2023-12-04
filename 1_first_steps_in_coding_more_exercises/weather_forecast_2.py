x = float(input())
if 26.00 <= x <= 35.00:
    print("Hot")
elif 20.1 <= x <= 25.9:
    print("Warm")
elif 15.00 <= x <= 20.00:
    print("Mild")
elif 12.00 <= x <= 14.9:
    print("Cool")
elif 5.00 <= x <= 11.9:
    print("Cold")
else:
    print("unknown")
