import random
from colorama import Fore

def random_password_only(mnay_user_and_password, length_password, users):
    for makes in range(mnay_user_and_password):
        lower = 'qwertyuiopasdfghjklzxcvbnm'
        numbers = '1234567890'
        symblos = '_.@!-'

        a11 = lower + numbers + symblos

        length_password = length_password
        password = "".join(random.sample(a11, length_password))

        THE_END = str(users)+':'+str(password)
        with open('combo_Random_password_only.txt', 'a') as save:
            save.write(THE_END + '\n')

    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Combo in file name ( {Fore.GREEN}combo_Random_password_only.txt{Fore.WHITE} )')