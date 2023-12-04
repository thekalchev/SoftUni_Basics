junior_bikers_count = int(input())
senior_bikers_count = int(input())
trace_type = input()
junior_tax = 0
senior_tax = 0
total_bikers = junior_bikers_count + senior_bikers_count
if trace_type == 'trail':
    junior_tax = 5.5
    senior_tax = 7
elif trace_type == 'cross-country':
    junior_tax = 8
    senior_tax = 9.5
    if total_bikers >= 50:
        junior_tax = junior_tax - junior_tax * .25
        senior_tax = senior_tax - senior_tax * .25
elif trace_type == 'downhill':
    junior_tax = 12.25
    senior_tax = 13.75
elif trace_type == 'road':
    junior_tax = 20
    senior_tax = 21.50

gross_income = senior_bikers_count * senior_tax + junior_bikers_count * junior_tax
net_income = gross_income - (gross_income * .05)
print(f'{net_income:.2f}')
