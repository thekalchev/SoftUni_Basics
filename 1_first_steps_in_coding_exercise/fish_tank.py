length = float(input())
width = float(input())
height = float(input())
percent_taken = float(input()) / 100
volume = length * width * height
volume_liters = volume * .001
print(volume_liters - (volume_liters * percent_taken))
