import random
from colorama import Fore

def random_user_only(mnay_user_and_password, length_user, password):
    for makes in range(mnay_user_and_password):
        lower = 'qwertyuiopasdfghjklzxcvbnm'
        numbers = '1234567890'
        symblos = '_.'

        a11 = lower + numbers + symblos

        length_USER = length_user
        USERS = "".join(random.sample(a11, length_USER))

        THE_END = str(USERS)+':'+str(password)
        with open('combo_Random_user_only.txt', 'a') as save:
            save.write(THE_END + '\n')

    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Combo in file name ( {Fore.GREEN}combo_Random_user_only.txt{Fore.WHITE} )')