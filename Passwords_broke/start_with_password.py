import random
from colorama import Fore


def start_with_password(mnay_passowrds, length_passwords, letters, start):
    for makes in range(mnay_passowrds):

        a11 = letters

        length = length_passwords

        password = "".join(random.sample(a11, length))

        the_end = start+password

        with open('Passwords_start_with.txt', 'a') as save:
            save.write(the_end + '\n')

    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make passwords in file name ( {Fore.GREEN}Passwords_satrt_with.txt{Fore.WHITE} )')