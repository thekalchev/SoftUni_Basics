judges_count = int(input())
total_averages = 0
average = 0
count = 0
while True:
    presentation = ''
    grades = 0
    count += 1
    presentation_name = input()
    total_averages += average
    if presentation_name == 'Finish':
        count -= 1
        print(f"Student's final assessment is {total_averages/count:.2f}.")
        exit()
    for i in range(judges_count):
        command = input()
        grade = float(command)
        grades += grade
        average = grades / judges_count
        presentation = presentation_name
    print(f'{presentation} - {average:.2f}.')
