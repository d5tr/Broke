import os

os.system('chmod +x Broke.sh')

XX = os.getcwd()
CLAN = str(XX)
cc =CLAN.replace('Broke', '')

os.system(f'cd {cc} && cp -r Broke /root')
os.system('mv Broke.sh /bin/Broke')

print('Done ... ')
