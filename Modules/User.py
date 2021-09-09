import random
from colorama import Fore


class Users :

    def __init__(self, mnay_passowrds='', length_passwords='', letters=''):

        self.mnay_passowrds = mnay_passowrds
        self.length_passwords = length_passwords
        self.letters = letters


    def random_users(self):
        for makes in range(self.mnay_passowrds):
            lower = 'qwertyuiopasdfghjklzxcvbnm'
            numbers = '1234567890'
            symblos = '_.'

            a11 = lower + numbers + symblos

            length = self.length_passwords

            password = "".join(random.sample(a11, length))

            with open('users_random.txt', 'a') as save:
                save.write(password + '\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Users in file name ( {Fore.GREEN}users_random.txt{Fore.WHITE} )')


    def your_choise_user(self):
        for makes in range(self.mnay_passowrds):

            a11 = self.letters

            length = self.length_passwords

            password = "".join(random.sample(a11, length))

            with open('Users_choise.txt', 'a') as save:
                save.write(password + '\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Users in file name ( {Fore.GREEN}Users_choise.txt{Fore.WHITE} )')