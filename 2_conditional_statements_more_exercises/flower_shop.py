from math import floor, ceil

magnolia = 3.25
ziumbiul = 4.00
roses = 3.50
cactuses = 8.00
magnolia_count = int(input())
ziumbiul_count = int(input())
roses_count = int(input())
cactuses_count = int(input())
gift_price = float(input())

revenue = magnolia * magnolia_count + ziumbiul_count * ziumbiul \
          + roses_count * roses + cactuses_count * cactuses
profit = revenue * .95
if profit >= gift_price:
    print(f"She is left with {floor(profit - gift_price)} leva.")
else:
    print(f"She will have to borrow {ceil(gift_price - profit)} leva.")
