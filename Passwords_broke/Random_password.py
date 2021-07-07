import random
from colorama import Fore

def random_passwords(mnay_passowrds, length_passwords):
    for makes in range(mnay_passowrds):
        lower = 'qwertyuiopasdfghjklzxcvbnm'
        upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        numbers = '1234567890'
        symblos = '-!@$_.'

        a11 = lower + upper + numbers + symblos

        length = length_passwords

        password = "".join(random.sample(a11, length))

        with open('Passwords_random.txt', 'a') as save:
            save.write(password + '\n')

    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make passwords in file name ( {Fore.GREEN}Passwords_random.txt{Fore.WHITE} )')
