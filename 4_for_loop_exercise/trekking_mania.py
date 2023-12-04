group_count = int(input())
mount = ''
musala_people = 0
monblan_people = 0
kilimandjaro_people = 0
k2_people = 0
everest_people = 0
for i in range(group_count):
    people_count = int(input())
    if people_count <= 5:
        mount = 'Musala'
        musala_people += people_count
    elif people_count <= 12:
        mount = 'Monblan'
        monblan_people += people_count
    elif people_count <= 25:
        mount = 'Kilimandjaro'
        kilimandjaro_people += people_count
    elif people_count <= 40:
        mount = 'K2'
        k2_people += people_count
    else:
        mount = 'Everest'
        everest_people += people_count

total_people = musala_people + monblan_people + kilimandjaro_people + k2_people + everest_people

percentage_musala = musala_people / total_people * 100
percentage_monblan = monblan_people / total_people * 100
percentage_kilimandjaro = kilimandjaro_people / total_people * 100
percentage_k2 = k2_people / total_people * 100
percentage_everest = everest_people / total_people * 100

print(f'{percentage_musala:.2f}%')  # musala
print(f'{percentage_monblan:.2f}%')  # monblan
print(f'{percentage_kilimandjaro:.2f}%')  # kilimandjaro
print(f'{percentage_k2:.2f}%')  # k2
print(f'{percentage_everest:.2f}%')  # everest