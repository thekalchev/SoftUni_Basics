days = ['Monday', 'Tuesday', 'Wednesday'
    , 'Thursday', 'Friday',
        'Saturday', 'Sunday']
day = int(input())
nums = [1, 2, 3, 4, 5, 6, 7]
if day in nums:
    print(days[day - 1])
else:
    print('Error')
