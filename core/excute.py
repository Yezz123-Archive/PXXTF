import os
import sys
import core
from time import sleep, time
from pxxtf import *
from core.exploit import clean
from core.banner import banner, PXXTF
# Set color
R = '\033[31m'  # Red
N = '\033[1;37m'  # White
G = '\033[32m'  # Green
O = '\033[0;33m'  # Orange
B = '\033[1;34m'  #Blue
E = '\033[0m'  # End
if not os.geteuid() == 0:  #Detected user root
    sys.exit(
        """\033[1;91m\n[!] Pentest Tools Framework run as root!!. \n\033[1;m"""
    )
if __name__ == "__main__" or clean() or banner() or PXXTF():
    main()


def main():
    while True:
        try:
            PXXTF = eval(input("Pentest>> "))
            if PXXTF == 'use modules/exploits':
                core.menu.exploits()
                main()
            elif PXXTF == 'use modules/scanners':
                core.menu.scan()
                main()
            elif PXXTF == 'use modules/password':
                core.menu.pas1()
                main()
            elif PXXTF == 'use modules/post':
                core.menu.post()
                main()
            elif PXXTF == 'use modules/listener':
                core.menu.listener()
                main()
            elif PXXTF == 'use modules/exploitdb':
                core.menu.exploit_db()
                main()
            elif PXXTF == 'use modules/tools':
                core.menu.tools()
                main()
            elif PXXTF == 'shell':
                core.exploit.commands()
                main()
            elif PXXTF == 'show modules':
                core.help.modules()
                main()
            elif PXXTF == 'ipconfig':
                core.exploit.ip1()
                main()
            elif PXXTF == 'show options':
                core.help.help()
                main()
            elif PXXTF == 'update':
                core.exploit.update()
                main()
            elif PXXTF == 'about':
                core.banner.info()
                main()
            elif PXXTF == 'credits':
                core.banner.credits()
                main()
            elif PXXTF == 'banner':
                clean(), banner(), PXXTF(), main()
            elif PXXTF == 'clear':
                core.menu.exploit.clean()
                main()
            elif PXXTF == 'exit':
                core.banner.exits()
                exit()
            else:
                print(("Wrong Command => ", PXXTF))
                print(("" + N + "" + B + "[" + R + "!" + B + "] " + N +
                    "Please enter 'show options'"))
                main()
        except (KeyboardInterrupt):
            print(
                ("\n" + R + "[*] (Ctrl + C ) Detected, Trying To Exit ...\n"))
            time.sleep(2)
            print(("" + G + "[*] Thank You For Using Pentest Framework =)\n"))
            time.sleep(3)
            exit()
