from math import floor

tournaments_count = int(input())
starting_points = int(input())

W = 2000
F = 1200
SF = 720

final_points = starting_points
wins = 0
for i in range(tournaments_count):
    reached_place = input()
    if reached_place == 'W':
        final_points += W
        wins += 1
    elif reached_place == 'F':
        final_points += F
    elif reached_place == 'SF':
        final_points += SF

average_points = (final_points - starting_points) / tournaments_count
percentage_wins = wins / tournaments_count * 100

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{percentage_wins:.2f}%')
