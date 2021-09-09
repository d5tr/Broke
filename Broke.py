from Modules.combo import *
from Modules.Password import *
from Modules.User import *
from Core.Broke_banners import *
from colorama import Fore
import os
from time import sleep
import time
from Modules.Info import *

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
    {Fore.LIGHTYELLOW_EX}[{Fore.RED}4{Fore.LIGHTYELLOW_EX}] INFO
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

            Make = Passwords(mnay_passowrds=M, length_passwords=L)
            Make.random_passwords()

        elif choose_password == 2 :
            clear()
            Broke_bnner()

            M = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter how many passwords you want : '))
            L = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length password : '))
            Letters = input(f'[{Fore.RED}?{Fore.WHITE}] Enter letters : ')

            Make = Passwords(mnay_passowrds=M, length_passwords=L, letters=Letters)
            Make.your_choise_password()

        elif choose_password == 3 :
            clear()
            Broke_bnner()

            M = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter how many passwords you want : '))
            L = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length password : '))
            Letters = input(f'[{Fore.RED}?{Fore.WHITE}] Enter letters : ')
            Start = input(f'[{Fore.RED}?{Fore.WHITE}] Enter word to start in password : ')

            Make = Passwords(mnay_passowrds=M, length_passwords=L, letters=Letters, start=Start)
            Make.start_with_password()

        elif choose_password == 4 :
            clear()
            Broke_bnner()

            M = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter how many passwords you want : '))
            L = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length password : '))
            Letters = input(f'[{Fore.RED}?{Fore.WHITE}] Enter letters : ')
            Ends = input(f'[{Fore.RED}?{Fore.WHITE}] Enter word to end in password : ')

            Make = Passwords(mnay_passowrds=M, length_passwords=L, letters=Letters, ends=Ends)
            Make.end_with_password()

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

            Make = Users(mnay_passowrds=many, length_passwords=length)
            Make.random_users()

        elif choose_user == 2 :
            clear()
            Broke_bnner()

            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many users you want : '))
            length = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length user : '))
            Letters = input(f'[{Fore.RED}?{Fore.WHITE}] Enter letters : ')

            Make = Users(mnay_passowrds=many, length_passwords=length, letters=Letters)

        elif choose_user == 99 :
            Broke()

    ################### For make combo ####################

    elif choose == 3 :
        clear()
        Broke_bnner()
        slowly(f'''
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}1{Fore.LIGHTYELLOW_EX}] Random passwords and users
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}2{Fore.LIGHTYELLOW_EX}] Random password only and user you choose it 
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}3{Fore.LIGHTYELLOW_EX}] Random user only and password you choose it
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}4{Fore.LIGHTYELLOW_EX}] Choose password letters 
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}5{Fore.LIGHTYELLOW_EX}] Choose user letters
        {Fore.LIGHTYELLOW_EX}[{Fore.RED}99{Fore.LIGHTYELLOW_EX}] Back
        
        {Fore.WHITE}
        ''')

        choose_combo = int(input(f'[{Fore.RED}?{Fore.WHITE}] Choose number : '))

        if choose_combo == 1 :
            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many passwords and users : '))
            L_user = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length users : '))
            L_passwords = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length passwords : '))


            Make = Combo(mnay_user_and_password=many, length_password=L_passwords, length_user=L_user)
            Make.random_combo_user_and_password()

        elif choose_combo == 2 :
            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many passwords and users : '))
            password = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length passwords : '))
            users = str(input(f'[{Fore.RED}?{Fore.WHITE}] Enter User : '))

            Make = Combo(mnay_user_and_password=many, length_password=password, users=users)
            Make.random_password_only()

        elif choose_combo == 3 :

            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many passwords and users : '))
            length_user = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length users : '))
            password = str(input(f'[{Fore.RED}?{Fore.WHITE}] Enter Password : '))

            Make = Combo(mnay_user_and_password=many, length_user=length_user, password=password)
            Make.random_user_only()

        elif choose_combo == 4 :
            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many passwords : '))
            length_password = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length password : '))
            LT = input(f'[{Fore.RED}?{Fore.WHITE}] Enter letters password : ')
            user = str(input(f'[{Fore.RED}?{Fore.WHITE}] Enter user : '))

            Make = Combo(mnay_user_and_password=many, length_password=length_password, users=user, password=LT)
            Make.choose_password_only()

        elif choose_combo == 5 :
            many = int(input(f'\n[{Fore.RED}?{Fore.WHITE}] Enter many users : '))
            length_user = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter length user : '))
            LU = input(f'[{Fore.RED}?{Fore.WHITE}] Enter letters user : ')
            password = str(input(f'[{Fore.RED}?{Fore.WHITE}] Enter password : '))

            Make = Combo(mnay_user_and_password=many, length_user=length_user, password=password, users=LU)
            Make.choose_user_only()


        elif choose_combo == 99 :
            Broke()
    
################### INFO ####################

    elif choose == 4 :
        print('\n')
        NAME = input(f'[{Fore.RED}?{Fore.WHITE}] Enter Name : ')
        AGE = input(f'[{Fore.RED}?{Fore.WHITE}] Enter Age : ')
        Date = input(f'[{Fore.RED}?{Fore.WHITE}] Enter Year of Birth : ')
        Name_web_site = input(f'[{Fore.RED}?{Fore.WHITE}] Enter name Web site : ')
        Some = input(f'[{Fore.RED}?{Fore.WHITE}] Enter Some thing he/she love : ')
        WORK = input(f'[{Fore.RED}?{Fore.WHITE}] Enter what is he/she work : ')
        NUMBER = input(f'[{Fore.RED}?{Fore.WHITE}] Enter Number : ')
        EMAIL = input(f'[{Fore.RED}?{Fore.WHITE}] Enter email without " @gmail.com Etc ...." : ')
        LENGTH = int(input(f'[{Fore.RED}?{Fore.WHITE}] Enter Length passwords : '))
        Many = int(input(f'[{Fore.RED}?{Fore.WHITE}] Entr many passwords you want : '))

        INfo(NAME, AGE, Date, Name_web_site, Some, WORK, NUMBER, EMAIL, LENGTH, Many)


    elif choose == 99 :
        print('\nGood bye ...')
        exit()

    else:
        print(f'{Fore.RED} \n Number not Found !')
        time.sleep(1)
        Broke()

# start tool
Broke()



