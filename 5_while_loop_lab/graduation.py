name= input()
is_excluded = False
times_failed = 0
current_grade = 1
total_grade = 0
while current_grade <= 12:
    year_grade = float(input())
    if year_grade < 4:
        times_failed += 1
        if times_failed > 1:
            print(f'{name} has been excluded at {current_grade} grade')
            break
        continue
    current_grade += 1
    total_grade += year_grade
average = total_grade / 12
if times_failed < 2:
    print(f'{name} graduated. Average grade: {average:.2f}')