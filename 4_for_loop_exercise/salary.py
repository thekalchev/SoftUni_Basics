open_tabs = int(input())
salary = float(input())
money_lost = 0

for tabs in range(open_tabs):
    website_name = input()
    if website_name == 'Facebook':
        money_lost += 150
    elif website_name == 'Instagram':
        money_lost += 100
    elif website_name == 'Reddit':
        money_lost += 50
    if money_lost >= salary:
        print('You have lost your salary.')
        exit()
if salary > money_lost:
    print(f'{salary - money_lost:.0f}')
