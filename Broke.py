from Passwords_broke.Random_password import *
from Broke_banners import *
from Passwords_broke.your_choise_password import *
from Passwords_broke.start_with_password import *
from Passwords_broke.end_with_password import *
from Users_broke.Random_users import *
from Users_broke.your_choise_user import *
from combo_broke.combo_Random_user_and_password import *
from combo_broke.random_password_only import *
from combo_broke.random_user_only import *
from colorama import Fore
import os
from time import sleep
import time

# For print slowly
def slowly(slows):
    for str in ' ' * 8 + slows + " \n":
        print(str, end="", flush=True)
        sleep(1 / 100)

#For clear
def clear():
    os.system('clear')

# The tool
def Broke():
    clear()
    # banner tool
    Broke_bnner()
    slowly(f'''
    {Fore.LIGHTYELLOW_EX}[{Fore.RED}1{Fore.LIGHTYELLOW_EX}] Passwords
    {Fore.LIGHTYELLOW_EX}[{Fore.RED}2{Fore.LIGHTYELLOW_EX}] Users
    {Fore.LIGHTYELLOW_EX}[{Fore.RED}3{Fore.LIGHTYELLOW_EX}] Combo
    {Fore.LIGHTYELLOW_EX}[{Fore.RED}99{Fore.LIGHTYELLOW_EX}] Exit {Fore.WHITE}
    
    ''')

    choose = int(input(f'\n [{Fore.RED}?{Fore.WHITE}] Choose number : '))


    ############### For make passwords ###############
    if choose == 1 :
        clear()
        Broke_bnner()

        slowly(f'''
    {Fore.LIGHTYELLOW_EX}[{Fore.RED}1{Fore.LIGHTYELLOW_EX}] Random passwords
    {Fore.LIGHTYELLOW_EX}[{Fore.RED}2{Fore.LIGHTYELLOW_EX}] Your choise of letters
    {Fore.LIGHTYELLOW_EX}[{Fore.RED}3{Fore.LIGHTYELLOW_EX}] Start with ( start password with word )
    {Fore.LIGHTYELLOW_EX}[{Fore.RED}4{Fore.LIGHTYELLOW_EX}] End with ( end password with word )
    {Fore.LIGHTYELLOW_EX}[{Fore.RED}99{Fore.LIGHTYELLOW_EX}] Back {Fore.WHITE}
    
        ''')
        choose_password = int(input(f'[{Fore.RED}?{Fore.WHITE}] Choose number : '))

        if choose_password == 1 :
            clear()
            Broke_bnner()

            M = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter how many passwords you want : '))
            L = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length password : '))

            random_passwords(M, L)

        elif choose_password == 2 :
            clear()
            Broke_bnner()

            M = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter how many passwords you want : '))
            L = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length password : '))
            Letters = input(f'[{Fore.RED}?{Fore.WHITE}] Enter letters : ')

            your_choise_password(M, L, Letters)

        elif choose_password == 3 :
            clear()
            Broke_bnner()

            M = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter how many passwords you want : '))
            L = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length password : '))
            Letters = input(f'[{Fore.RED}?{Fore.WHITE}] Enter letters : ')
            start = input(f'[{Fore.RED}?{Fore.WHITE}] Enter word to start in password : ')

            start_with_password(M, L, Letters, start)

        elif choose_password == 4 :
            clear()
            Broke_bnner()

            M = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter how many passwords you want : '))
            L = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length password : '))
            Letters = input(f'[{Fore.RED}?{Fore.WHITE}] Enter letters : ')
            ends = input(f'[{Fore.RED}?{Fore.WHITE}] Enter word to end in password : ')

            end_with_password(M, L, Letters, ends)

        elif choose_password == 99 :
            Broke()
    ############### End for make passwords ###############

    ############## For make users ################

    elif choose == 2 :
        clear()
        Broke_bnner()

        slowly(f'''
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}1{Fore.LIGHTYELLOW_EX}] Random Users
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}2{Fore.LIGHTYELLOW_EX}] Your choise of letters
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}99{Fore.LIGHTYELLOW_EX}] Back {Fore.WHITE}

            ''')

        choose_user = int(input(f'[{Fore.RED}?{Fore.WHITE}] Choose number : '))

        if choose_user == 1 :

            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many users you want : '))
            length = int(input(f'[F{Fore.RED}?{Fore.WHITE}] Enter length user : '))

            random_users(many, length)

        elif choose_user == 2 :
            clear()
            Broke_bnner()

            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many users you want : '))
            length = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length user : '))
            letters = input(f'[{Fore.RED}?{Fore.WHITE}] Enter letters : ')

            your_choise_user(many, length, letters)

        elif choose_user == 99 :
            Broke()

    elif choose == 3 :
        clear()
        Broke_bnner()
        slowly(f'''
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}1{Fore.LIGHTYELLOW_EX}] Random passwords and users
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}2{Fore.LIGHTYELLOW_EX}] Random password only and user you choose it 
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}3{Fore.LIGHTYELLOW_EX}] Random user only and password you choose it
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}99{Fore.LIGHTYELLOW_EX}] Back
        
        {Fore.WHITE}
        ''')

        choose_combo = int(input(f'[{Fore.RED}?{Fore.WHITE}] Choose number : '))

        if choose_combo == 1 :
            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many passwords and users : '))
            L_user = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length users : '))
            L_passwords = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length passwords : '))


            random_combo_user_and_password(many, L_user, L_passwords)

        elif choose_combo == 2 :
            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many passwords and users : '))
            password = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length passwords : '))
            users = str(input(f'[{Fore.RED}?{Fore.WHITE}] Enter User : '))

            random_password_only(many,password, users)

        elif choose_combo == 3 :

            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many passwords and users : '))
            length_user = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length users : '))
            password = str(input(f'[{Fore.RED}?{Fore.WHITE}] Enter Password : '))

            random_user_only(many, length_user, password)

        elif choose_combo == 99 :
            Broke()




    elif choose == 99 :
        print('\nGood bye ...')
        exit()

    else:
        print(f'{Fore.RED} \n Number not Found !')
        time.sleep(1)
        Broke()

# start tool
Broke()



