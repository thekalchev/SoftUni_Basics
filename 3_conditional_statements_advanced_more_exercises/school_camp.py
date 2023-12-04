season = input()
group_type = input()
count_students = int(input())
count_nights = int(input())
price_night = 0
sport = ''

if season == 'Winter':
    if group_type == 'boys':
        price_night = 9.6
        sport = 'Judo'
    elif group_type == 'girls':
        price_night = 9.6
        sport = 'Gymnastics'
    elif group_type == 'mixed':
        price_night = 10
        sport = 'Ski'

elif season == 'Spring':
    if group_type == 'boys':
        price_night = 7.2
        sport = 'Tennis'
    elif group_type == 'girls':
        price_night = 7.2
        sport = 'Athletics'
    elif group_type == 'mixed':
        price_night = 9.5
        sport = 'Cycling'

elif season == 'Summer':
    if group_type == 'boys':
        price_night = 15
        sport = 'Football'
    elif group_type == 'girls':
        price_night = 15
        sport = 'Volleyball'
    elif group_type == 'mixed':
        price_night = 20
        sport = 'Swimming'

price_vacation = price_night * count_nights * count_students
if count_students >= 50:
    price_vacation *= .50
elif 20 <= count_students < 50:
    price_vacation *= .85
elif 10 <= count_students < 20:
    price_vacation *= .95

print(f'{sport} {price_vacation:.2f} lv.')
