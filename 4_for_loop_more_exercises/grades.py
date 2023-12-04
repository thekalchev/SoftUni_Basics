students_count = int(input())
excellent = 0
good = 0
bad = 0
fail = 0
grades = 0
for student in range(students_count):
    grade = float(input())
    if 2 <= grade <= 2.99:
        fail += 1
        grades += grade
    if 3 <= grade <= 3.99:
        bad += 1
        grades += grade

    if 4 <= grade <= 4.99:
        good += 1
        grades += grade

    if grade >= 5:
        excellent += 1
        grades += grade

total_grades = excellent + good + bad + fail
excellent_per = excellent / total_grades * 100
good_per = good / total_grades * 100
bad_per = bad / total_grades * 100
fail_per = fail / total_grades * 100
average = grades / total_grades
print(f'Top students: {excellent_per:.2f}%')
print(f'Between 4.00 and 4.99: {good_per:.2f}%')
print(f'Between 3.00 and 3.99: {bad_per:.2f}%')
print(f'Fail: {fail_per:.2f}%')
print(f'Average: {average:.2f}')
