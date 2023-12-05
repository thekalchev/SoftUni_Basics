width = int(input())
length = int(input())
hight = int(input())
space_available = width * length * hight

while True:
    command = input()

    if command == 'Done':
        print(f'{abs(space_available)} Cubic meters left.')
        break

    space_to_take = int(command)
    if 0 < space_available:
        space_available -= space_to_take
        if space_available <= 0:
            print(f'No more free space! You need {abs(space_available)} Cubic meters more.')
            break


