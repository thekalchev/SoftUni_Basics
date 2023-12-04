hour = float(input())
week_day = input()
work_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
work_hours = [10,11,12,13,14,15,16,17,18]
if week_day in work_days:
    if hour in work_hours:
        print('open')
    else:
        print('closed')
else:
    print('closed')
