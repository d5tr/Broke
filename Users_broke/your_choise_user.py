import random
from colorama import Fore

def your_choise_user(mnay_passowrds, length_passwords, letters):
    for makes in range(mnay_passowrds):

        a11 = letters

        length = length_passwords

        password = "".join(random.sample(a11, length))

        with open('Users_choise.txt', 'a') as save:
            save.write(password + '\n')

    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Users in file name ( {Fore.GREEN}Users_choise.txt{Fore.WHITE} )')
