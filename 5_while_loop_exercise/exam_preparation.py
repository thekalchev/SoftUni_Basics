failed_treshold = int(input())
failed_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ''
has_failed = True
while failed_times < failed_treshold:
    problem_name = input()
    if problem_name == 'Enough':
        break
    elif problem_name != 'Enough':
        last_problem = problem_name
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems_count += 1
average = grades_sum / solved_problems_count
if failed_times < failed_treshold:
    print(f'Average score: {average:.2f}')
    print(f'Number of problems: {solved_problems_count}')
    print(f'Last problem: {last_problem}')
else:
    print(f'You need a break, {failed_times} poor grades.')