budget = float(input())
videocards_count = float(input())
processors_count = float(input())
ram_count = float(input())

videocard_price = 250
processor_price = videocards_count * videocard_price * .35
ram_price = videocard_price * videocards_count * .10

total_price = videocard_price * videocards_count + \
              processor_price * processors_count + \
              ram_price * ram_count
if videocards_count > processors_count:
    total_price *= .85

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
