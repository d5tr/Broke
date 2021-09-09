import random
from colorama import Fore

def INfo(Name='', Age='', Date='', nameWebSIte='', what_he_love='', work='', number='', email='', lengthx='', many=''):

    for CC in range(int(many)):
        A11 = str(Name)+str(Age)+str(Date)+str(nameWebSIte)+str(what_he_love)+str(work)+str(number)+str(email)

        length = lengthx

        Find = "".join(random.sample(A11, length))
        
        with open('INFO.txt', 'a') as Save :
            Save.write(Find+'\n')
    
    X7 = str(Name)+str(Age)
    Ok = str(number)+str(Name)
    Kill = str(Name)+str(Date)
    lux = str(Name)+str(number)

    with open('INFO.txt', 'a') as W :
        W.write(X7+'\n') 

    with open('INFO.txt', 'a') as C4 :
        C4.write(Ok+'\n')

    with open('INFO.txt', 'a') as E3 :
        E3.write(Kill+'\n')

    with open('INFO.txt', 'a') as Z1 :
        Z1.write(lux+'\n')

    print(f'[{Fore.GREEN}+{Fore.WHITE}] Done make password list and save in file name ( {Fore.GREEN}INFO.txt{Fore.WHITE} ) ... ')
    