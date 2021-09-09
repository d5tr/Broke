import random
from colorama import Fore


class Passwords :

    def __init__(self, mnay_passowrds='', length_passwords='', letters='', ends='', start=''):

        self.mnay_passowrds = mnay_passowrds
        self.length_passwords = length_passwords
        self.letters = letters
        self.ends = ends
        self.start = start


    def end_with_password(self):
        for makes in range(self.mnay_passowrds):

            a11 = self.letters

            length = self.length_passwords

            password = "".join(random.sample(a11, length))

            the_end = password+self.ends

            with open('Passwords_end_with.txt', 'a') as save:
                save.write(the_end + '\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make passwords in file name ( {Fore.GREEN}Passwords_end_with.txt{Fore.WHITE} )')


    def random_passwords(self):
        for makes in range(self.mnay_passowrds):
            lower = 'qwertyuiopasdfghjklzxcvbnm'
            upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
            numbers = '1234567890'
            symblos = '-!@$_.'

            a11 = lower + upper + numbers + symblos

            length = self.length_passwords

            password = "".join(random.sample(a11, length))

            with open('Passwords_random.txt', 'a') as save:
                save.write(password + '\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make passwords in file name ( {Fore.GREEN}Passwords_random.txt{Fore.WHITE} )')

    
    def start_with_password(self):
        for makes in range(self.mnay_passowrds):

            a11 = self.letters

            length = self.length_passwords

            password = "".join(random.sample(a11, length))

            the_end = self.start+password

            with open('Passwords_start_with.txt', 'a') as save:
                save.write(the_end + '\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make passwords in file name ( {Fore.GREEN}Passwords_satrt_with.txt{Fore.WHITE} )')

    
    def your_choise_password(self):
        for makes in range(self.mnay_passowrds):

            a11 = self.letters

            length = self.length_passwords

            password = "".join(random.sample(a11, length))

            with open('Passwords_choise.txt', 'a') as save:
                save.write(password + '\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make passwords in file name ( {Fore.GREEN}Passwords_choise.txt{Fore.WHITE} )')