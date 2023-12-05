while True:
    destination = input()
    if destination == 'End':
        exit()
    minimal_budet = float(input())
    total_money_saved = 0
    while True:
        command = input()
        if command == 'End':
            exit()
        money_saved = float(command)
        total_money_saved += money_saved
        if total_money_saved >= minimal_budet:
            print(f'Going to {destination}!')
            break