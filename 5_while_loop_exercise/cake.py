length = int(input())
width = int(input())
pieces_count = length * width

while True:
    command = input()
    if command == 'STOP':
        print(f'{pieces_count} pieces are left.')
        break


    elif pieces_count > 0:
        pieces_count -= int(command)
        if pieces_count <= 0:
            print(f'No more cake left! You need {abs(pieces_count)} pieces more.')
            break

    else:
        break
