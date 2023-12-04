num = int(input())
if num <= 100:
    if num % 2 == 0:
        print(6)
        print(num + 6)
    elif num % 5 == 0:
        print(7)
        print(num + 7)
    else:
        print(5)
        print(num + 5)

elif 100 < num <= 1000:
    if num % 2 == 0:
        print(num * .2 + 1)
        print(1.2 * num + 1)
    elif num % 5 == 0:
        print(num * .2 + 2)
        print(1.2 * num + 2)
    else:
        print(num * .2)
        print(num * 1.2)
else:
    if num % 2 == 0:
        print(num * .1 + 1)
        print(num * 1.1 + 1)
    elif num % 5 == 0:
        print(num * .1 + 2)
        print(num * 1.1 + 2)
    else:
        print(num * .1)
        print(num * 1.1)
