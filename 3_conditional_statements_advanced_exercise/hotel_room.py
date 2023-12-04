month = input()
nights = int(input())
type_room = ''
studio_price_night = 0
studio_total_price = 0
apartment_price_night = 0
apartment_total_price = 0

if month == "May" or month == 'October':
    studio_price_night = 50
    apartment_price_night = 65
    studio_total_price = studio_price_night * nights
    apartment_total_price = apartment_price_night * nights
    if 7 < nights < 14:
        studio_total_price = studio_price_night * nights * .95
    elif nights > 14:
        studio_total_price = studio_price_night * nights * .7
        apartment_total_price = apartment_price_night * nights * .9

elif month == "June" or month == "September":
    studio_price_night = 75.2
    apartment_price_night = 68.7
    studio_total_price = studio_price_night * nights
    apartment_total_price = apartment_price_night * nights
    if nights > 14:
        studio_total_price = studio_price_night * nights * .8
        apartment_total_price = apartment_price_night * nights * .9

elif month == "July" or month == "August":
    studio_price_night = 76
    apartment_price_night = 77
    studio_total_price = studio_price_night * nights
    apartment_total_price = apartment_price_night * nights
    if nights > 14:
        apartment_total_price = apartment_price_night * nights * .9

print(f'Apartment: {apartment_total_price:.2f} lv.')
print(f'Studio: {studio_total_price:.2f} lv.')
