stadium_capacity = int(input())
total_fans = int(input())
A = 0
B = 0
V = 0
G = 0
for fan in range(total_fans):
    sector = input()
    if sector == 'A':
        A += 1
    elif sector == 'B':
        B += 1
    elif sector == 'V':
        V += 1
    elif sector == 'G':
        G += 1
total = A + B + V + G
A_per = A / total * 100
B_per = B / total * 100
V_per = V / total * 100
G_per = G / total * 100
capacity_full = total / stadium_capacity * 100
print(f'{A_per:.2f}%')
print(f'{B_per:.2f}%')
print(f'{V_per:.2f}%')
print(f'{G_per:.2f}%')
print(f'{capacity_full:.2f}%')
