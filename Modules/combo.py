import random
from colorama import Fore

class Combo :

    def __init__(self, mnay_user_and_password='', length_user='', length_password='', users='', password=''):

        self.mnay_user_and_password = mnay_user_and_password
        self.length_user = length_user
        self.length_password = length_password 
        self.users = users
        self.password = password
        

    def random_combo_user_and_password(self):
        for makes in range(self.mnay_user_and_password):
            lower = 'qwertyuiopasdfghjklzxcvbnm'
            numbers = '1234567890'
            symblos = '_.'

            a11 = lower + numbers + symblos

            length_user = self.length_user
            length_password = self.length_password
            password = "".join(random.sample(a11, length_password))
            user = "".join(random.sample(a11, length_user))
            THE_END = str(user)+':'+str(password)
            with open('combo_Random_user_and_password.txt', 'a') as save:
                save.write(THE_END + '\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Combo in file name ( {Fore.GREEN}combo_Random_user_and_password.txt{Fore.WHITE} )')

    
    def random_password_only(self):
        for makes in range(self.mnay_user_and_password):
            lower = 'qwertyuiopasdfghjklzxcvbnm'
            numbers = '1234567890'
            symblos = '_.@!-'

            a11 = lower + numbers + symblos

            length_password = self.length_password
            password = "".join(random.sample(a11, length_password))

            THE_END = str(self.users)+':'+str(password)
            with open('combo_Random_password_only.txt', 'a') as save:
                save.write(THE_END + '\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Combo in file name ( {Fore.GREEN}combo_Random_password_only.txt{Fore.WHITE} )')
        
    
    def random_user_only(self):
        for makes in range(self.mnay_user_and_password):
            lower = 'qwertyuiopasdfghjklzxcvbnm'
            numbers = '1234567890'
            symblos = '_.'

            a11 = lower + numbers + symblos

            length_USER = self.length_user
            USERS = "".join(random.sample(a11, length_USER))

            THE_END = str(USERS)+':'+str(self.password)
            with open('combo_Random_user_only.txt', 'a') as save:
                save.write(THE_END + '\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Combo in file name ( {Fore.GREEN}combo_Random_user_only.txt{Fore.WHITE} )')

    
    def choose_password_only(self):

        for makes in range(self.mnay_user_and_password):

            a11 = self.password

            length = self.length_password

            AP = "".join(random.sample(a11, length))

            THE_END = str(self.users)+':'+(AP)

            with open('combo_choose_password_only.txt', 'a') as save :
                save.write(THE_END+'\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Combo in file name ( {Fore.GREEN}combo_choose_password_only.txt{Fore.WHITE} )')

    
    def choose_user_only(self):

        for makes in range(self.mnay_user_and_password):

            a11 = self.users

            length = self.length_user

            AP = "".join(random.sample(a11, length))

            THE_END = str(AP)+':'+(self.password)

            with open('combo_choose_user_only.txt', 'a') as save :
                save.write(THE_END+'\n')

        print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make Combo in file name ( {Fore.GREEN}combo_choose_user_only.txt{Fore.WHITE} )')



