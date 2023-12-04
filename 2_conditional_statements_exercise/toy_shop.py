puzzle_price = 2.60
talking_doll_price = 3.00
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

trip_price = float(input())
puzzles_count = float(input())
talking_dolls_count = float(input())
teddy_bears_count = float(input())
minions_count = float(input())
trucks_count = float(input())

total_count = puzzles_count + talking_dolls_count \
              + teddy_bears_count + minions_count + trucks_count
money_earned = puzzle_price * puzzles_count + talking_dolls_count * talking_doll_price \
               + teddy_bear_price * teddy_bears_count \
               + minions_count * minion_price + truck_price * trucks_count

if total_count >= 50:
    money_earned = money_earned - money_earned * .25

money_earned = money_earned - money_earned * .1

if money_earned >= trip_price:
    print(f"Yes! {money_earned - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - money_earned:.2f} lv needed.")
