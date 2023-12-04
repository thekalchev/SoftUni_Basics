cargo_count = int(input())
tones_by_microbus = 0
tones_by_truck = 0
tones_by_train = 0
price_per_tone = 0
for i in range(cargo_count):
    cargo_weight = int(input())
    if cargo_weight <= 3:
        price_per_tone = 200
        tones_by_microbus += cargo_weight
    elif 4 <= cargo_weight <= 11:
        price_per_tone = 175
        tones_by_truck += cargo_weight
    elif cargo_weight >= 12:
        price_per_tone = 120
        tones_by_train += cargo_weight
total_weight = tones_by_train + tones_by_microbus + tones_by_truck

train_average = tones_by_train / total_weight * 100
truck_average = tones_by_truck / total_weight * 100
microbus_average = tones_by_microbus / total_weight * 100
average_price = (tones_by_microbus * 200 + tones_by_truck * 175 + tones_by_train * 120) / total_weight
print(f'{average_price:.2f}')
print(f'{microbus_average:.2f}%')
print(f'{truck_average:.2f}%')
print(f'{train_average:.2f}%')
