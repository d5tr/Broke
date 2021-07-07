import random
from colorama import Fore

def your_choise_password(mnay_passowrds, length_passwords, letters):
    for makes in range(mnay_passowrds):

        a11 = letters

        length = length_passwords

        password = "".join(random.sample(a11, length))

        with open('Passwords_choise.txt', 'a') as save:
            save.write(password + '\n')

    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make passwords in file name ( {Fore.GREEN}Passwords_choise.txt{Fore.WHITE} )')

