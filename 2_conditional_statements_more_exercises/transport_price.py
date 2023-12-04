kilometers_to_travel = float(input())
day_or_night = input()
taxi_day = .79
taxi_night = .90
bus = .09  # za razstoqniq minimum 20km
train = .06  # za razstoqniq minimum 100km
best_price = 0

if kilometers_to_travel >= 100:
    best_price = kilometers_to_travel * train
    print(f"{best_price:.2f}")
elif kilometers_to_travel >= 20:
    best_price = kilometers_to_travel * bus
    print(f"{best_price:.2f}")
else:
    if day_or_night == "night":
        best_price = kilometers_to_travel * taxi_night
        print(f"{best_price + .7:.2f}")
    elif day_or_night == "day":
        best_price = kilometers_to_travel * taxi_day
        print(f"{best_price + .7:.2f}")
