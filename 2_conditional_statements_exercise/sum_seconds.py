x, y, z = int(input()), int(input()), int(input())
total = x + y + z
mins = total // 60
secs = total % 60
if secs < 10:
    print(f"{mins}:0{secs}")
else:
    print(f"{mins}:{secs}")
