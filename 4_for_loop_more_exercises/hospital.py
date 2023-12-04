period = int(input())  # Въвеждаме периода
doctors = 7  # Начален брой лекари
treated_patients = 0  # Брой прегледани пациенти
untreated_patients = 0  # Брой непрегледани пациенти

for _ in range(1, period + 1):
    patients = int(input())  # Брой пациенти за текущия ден

    if patients <= doctors:
        treated_patients += patients
    else:
        treated_patients += doctors
        untreated_patients += patients - doctors

    if _ % 3 == 2 and untreated_patients > treated_patients:
        doctors += 1

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
