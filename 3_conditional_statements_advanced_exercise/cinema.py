projection = input()
rows = int(input())
columns = int(input())

income = 0
if projection == "Premiere":
    income = 12 * rows * columns
elif projection == 'Normal':
    income = 7.5 *rows *columns
elif projection == 'Discount':
    income = 5 * rows * columns
print(f"{income:.2f} leva")