import os
import sys
import core
from time import sleep, time
from core.exploit import clean
from core.banner import banner, ptf
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
if __name__ == "__main__" or clean() or banner() or ptf():
    main()


def main():
    while True:
        try:
            ptf = eval(input("Pentest>> "))
            if ptf == 'use modules/exploits':
                core.menu.exploits()
                main()
            elif ptf == 'use modules/scanners':
                core.menu.scan()
                main()
            elif ptf == 'use modules/password':
                core.menu.pas1()
                main()
            elif ptf == 'use modules/post':
                core.menu.post()
                main()
            elif ptf == 'use modules/listener':
                core.menu.listener()
                main()
            elif ptf == 'use modules/exploitdb':
                core.menu.exploit_db()
                main()
            elif ptf == 'use modules/tools':
                core.menu.tools()
                main()
            elif ptf == 'shell':
                core.exploit.commands()
                main()
            elif ptf == 'show modules':
                core.help.modules()
                main()
            elif ptf == 'ipconfig':
                core.exploit.ip1()
                main()
            elif ptf == 'show options':
                core.help.help()
                main()
            elif ptf == 'update':
                core.exploit.update()
                main()
            elif ptf == 'about':
                core.banner.info()
                main()
            elif ptf == 'credits':
                core.banner.credits()
                main()
            elif ptf == 'banner':
                clean(), banner(), ptf(), main()
            elif ptf == 'clear':
                core.menu.exploit.clean()
                main()
            elif ptf == 'exit':
                core.banner.exits()
                exit()
            else:
                print(("Wrong Command => ", ptf))
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
