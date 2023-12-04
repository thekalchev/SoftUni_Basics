from math import floor

world_record = float(input())
distance = float(input())
seconds_per_meter = float(input())
time = distance * seconds_per_meter
resistance = distance // 15 * 12.5
total_time_ivan = time + resistance
if total_time_ivan >= world_record:
    print(f"No, he failed! He was {total_time_ivan - world_record:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time_ivan:.2f} seconds.")
