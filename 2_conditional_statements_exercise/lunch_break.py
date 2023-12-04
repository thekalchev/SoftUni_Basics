from math import ceil

tv_show_name = input()
length_episode = float(input())
break_time = float(input())

lunch_time = break_time * .125
relax_time = break_time * .25

leftover_time = break_time - lunch_time - relax_time
if leftover_time >= length_episode:
    print(f"You have enough time to watch {tv_show_name} and "
          f"left with {ceil(leftover_time - length_episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show_name},"
          f" you need {ceil(length_episode - leftover_time)} more minutes. ")
