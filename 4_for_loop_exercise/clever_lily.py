lilly_age = int(input())
price_washer = float(input())
single_toy_price = int(input())

total_cash = 0

for birthday in range(1, lilly_age + 1):
    if birthday % 2 == 0:
        total_cash += birthday * 5
        total_cash -= 1
    else:
        total_cash += single_toy_price

if total_cash >= price_washer:
    print(f'Yes! {total_cash - price_washer:.2f}')
else:
    print(f'No! {price_washer - total_cash:.2f}')
