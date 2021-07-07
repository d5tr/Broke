import random
from colorama import Fore

def random_users(mnay_passowrds, length_passwords):
    for makes in range(mnay_passowrds):
        lower = 'qwertyuiopasdfghjklzxcvbnm'
        numbers = '1234567890'
        symblos = '_.'

        a11 = lower + numbers + symblos

        length = length_passwords

        password = "".join(random.sample(a11, length))

        with open('users_random.txt', 'a') as save:
            save.write(password + '\n')

    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Users in file name ( {Fore.GREEN}users_random.txt{Fore.WHITE} )')