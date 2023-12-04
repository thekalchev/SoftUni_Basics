actor_name = input()
academy_points = float(input())
judges = int(input())
total_points = academy_points
for i in range(judges):
    judge_name = input()
    judge_points = float(input())
    total_points += len(judge_name) * judge_points / 2
    if total_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break
if (total_points) < 1250.5:
    print(f'Sorry, {actor_name} you need {1250.5 - (total_points):.1f} more!')
