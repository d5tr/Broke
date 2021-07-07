import random
from colorama import Fore

def random_combo_user_and_password(mnay_user_and_password, length_user, length_password):
    for makes in range(mnay_user_and_password):
        lower = 'qwertyuiopasdfghjklzxcvbnm'
        numbers = '1234567890'
        symblos = '_.'

        a11 = lower + numbers + symblos

        length_user = length_user
        length_password = length_password
        password = "".join(random.sample(a11, length_password))
        user = "".join(random.sample(a11, length_user))
        THE_END = str(user)+':'+str(password)
        with open('combo_Random_user_and_password.txt', 'a') as save:
            save.write(THE_END + '\n')

    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Combo in file name ( {Fore.GREEN}combo_Random_user_and_password.txt{Fore.WHITE} )')