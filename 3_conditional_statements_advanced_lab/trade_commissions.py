city = input()
sales = float(input())
sales_commission = 0

if city == 'Sofia':
    if 0 <= sales <= 500:
        sales_commission = sales * .05
        print(f"{sales_commission:.2f}")

    elif 500 < sales <= 1000:
        sales_commission = sales * .07
        print(f"{sales_commission:.2f}")

    elif 1000 < sales <= 10000:
        sales_commission = sales * .08
        print(f"{sales_commission:.2f}")

    elif sales > 10000:
        sales_commission = sales * .12
        print(f"{sales_commission:.2f}")

    else:
        print('error')

elif city == 'Varna':
    if 0 <= sales <= 500:
        sales_commission = sales * .045
        print(f"{sales_commission:.2f}")

    elif 500 < sales <= 1000:
        sales_commission = sales * .075
        print(f"{sales_commission:.2f}")

    elif 1000 < sales <= 10000:
        sales_commission = sales * .1
        print(f"{sales_commission:.2f}")

    elif sales > 10000:
        sales_commission = sales * .13
        print(f"{sales_commission:.2f}")

    else:
        print('error')

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        sales_commission = sales * .055
        print(f"{sales_commission:.2f}")

    elif 500 < sales <= 1000:
        sales_commission = sales * .08
        print(f"{sales_commission:.2f}")

    elif 1000 < sales <= 10000:
        sales_commission = sales * .12
        print(f"{sales_commission:.2f}")

    elif sales > 10000:
        sales_commission = sales * .145
        print(f"{sales_commission:.2f}")

    else:
        print('error')
else:
    print('error')
