rest_days_count = int(input())
work_days_count = 365 - rest_days_count
norm_good_sleep = 30000  # mins per year
work_day_play = 63  # mins per day
rest_day_play = 127  # mins per day

total_play = rest_days_count * 127 + work_days_count * 63

underplay = norm_good_sleep - total_play
hours = underplay // 60
minutes = underplay % 60

overplay = total_play - norm_good_sleep
hours_overplay = overplay // 60
minutes_overplay = overplay % 60

if norm_good_sleep > total_play:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours_overplay} hours and {minutes_overplay} minutes more for play")
