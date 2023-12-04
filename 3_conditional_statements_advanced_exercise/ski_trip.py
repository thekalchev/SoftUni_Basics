days_of_stay = int(input())
type_of_accomodation = input()
review = input()

room_for_one_night = 18
apartment_night = 25
president_apartment_night = 35
total_price = 0
nights_of_stay = ''

if type_of_accomodation == 'room for one person':
    total_price = (days_of_stay - 1) * room_for_one_night
    if review == 'positive':
        total_price = (days_of_stay - 1) * room_for_one_night * 1.25
    elif review == 'negative':
        total_price = (days_of_stay - 1) * room_for_one_night * .90

elif type_of_accomodation == 'apartment':
    total_price = (days_of_stay - 1) * apartment_night
    if days_of_stay < 10:
        total_price = total_price * .7
        if review == 'positive':
            total_price = total_price * 1.25
        elif review == 'negative':
            total_price = total_price * .9
    elif 10 <= days_of_stay <= 15:
        total_price = total_price * .65
        if review == 'positive':
            total_price = total_price * 1.25
        elif review == 'negative':
            total_price = total_price * .9
    elif days_of_stay > 15:
        total_price = total_price * .5
        if review == 'positive':
            total_price = total_price * 1.25
        elif review == 'negative':
            total_price = total_price * .9


elif type_of_accomodation == 'president apartment':
    total_price = (days_of_stay - 1) * president_apartment_night
    if days_of_stay < 10:
        total_price = total_price * .9
    elif 10 <= days_of_stay <= 15:
        total_price = total_price * .85
    elif days_of_stay > 15:
        total_price = total_price * .8
    if review == 'positive':
        total_price = total_price * 1.25
    if review == 'negative':
        total_price = total_price * .9

print(f'{total_price:.2f}')
