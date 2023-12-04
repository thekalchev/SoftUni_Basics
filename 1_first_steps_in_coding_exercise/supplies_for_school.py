pens = float(input()) * 5.80
markers = float(input()) * 7.20
detergent = float(input()) * 1.20
discount = float(input()) / 100
total = pens + markers + detergent
total_with_discount = total - total * discount
print(total_with_discount)
