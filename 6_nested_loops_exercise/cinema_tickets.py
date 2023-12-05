# movie_name = input()
# seats_available = int(input())
# seats_taken = 0
# total_tickets = 0
# student_tickets = 0
# standard_tickets = 0
# kids_tickets = 0
# taken = (seats_taken / seats_available) * 100
#
# while True:
#     ticket_type = input()
#     taken = (seats_taken / seats_available)* 100
#     if ticket_type == 'Finish':
#         print(f'{movie_name} - {taken:.2f}% full')
#         break
#     elif ticket_type == 'End':
#         print(f'{movie_name} - {taken:.2f}% full')
#
#         movie_name = input()
#         if movie_name == 'Finish':
#             print(f'{movie_name} - {taken:.2f}% full')
#             break
#         seats_available = int(input())
#         continue
#     elif ticket_type == 'student':
#         student_tickets += 1
#     elif ticket_type == 'kid':
#         kids_tickets += 1
#     elif ticket_type == 'standard':
#         standard_tickets += 1
#     taken += 1
#     seats_taken += 1
#     total_tickets += 1
#     if taken > seats_available:
#         taken = 100
# standard_tickets_per = (standard_tickets/ total_tickets) * 100
# kids_tickets_per = (kids_tickets/ total_tickets) * 100
# student_tickets_per = (student_tickets/ total_tickets) * 100
# print(f'Total tickets: {total_tickets}')
# print(f'{student_tickets_per:.2f}% student tickets.')
# print(f'{standard_tickets_per:.2f}% standard tickets.')
# print(f'{kids_tickets_per:.2f}% kids tickets.')
#
#
total_tickets = 0
command = input()
students_total = 0
standard_total = 0
kids_total = 0
while command != 'Finish':
    current_movie = command
    total_seats = int(input())
    available_seats = total_seats

    while available_seats > 0:
        current_ticket_type = input()  # End or [student,standard,kid]
        if current_ticket_type == 'End':
            break
        available_seats -= 1
        if current_ticket_type == 'student':
            students_total += 1
        elif current_ticket_type == 'standard':
            standard_total += 1
        elif current_ticket_type == 'kid':
            kids_total += 1

    seats_bought = (total_seats - available_seats)
    total_tickets += seats_bought

    percent_full = (total_seats - available_seats) / total_seats * 100
    print(f'{current_movie} - {percent_full:.2f}% full.')

    command = input()

percent_students = students_total / total_tickets * 100
percent_standard = standard_total / total_tickets * 100
percent_kids = kids_total / total_tickets * 100

print(f'Total tickets: {total_tickets}')
print(f'{percent_students:.2f}% student tickets.')
print(f'{percent_standard:.2f}% standard tickets.')
print(f'{percent_kids:.2f}% kids tickets.')
