name = input()
correct_password = input()
password_guess = input()
while password_guess != correct_password:
    password_guess = input()
print(f'Welcome {name}!')