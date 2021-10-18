import os,time,sys
import core
from time import sleep
from ptf import *
from core.exploit import clean
from core.banner import banner,ptf
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
if os.geteuid() != 0:#Detected user root
    sys.exit("""\033[1;91m\n[!] Pentest Tools Framework run as root!!. \n\033[1;m""")
if __name__ == "__main__" or clean() or banner() or ptf():
    main()
def main():
    while True:
            try:
                PTF = raw_input("Pentest>> ")
                if PTF == 'use modules/exploits':
                    core.menu.exploits()
                    main()
                elif PTF == 'use modules/scanners':
                    core.menu.scan()
                    main()
                elif PTF =='use modules/password':
                    core.menu.pas1()
                    main()
                elif PTF == 'use modules/post':
                    core.menu.post()
                    main()
                elif PTF =='use modules/listener':
                    core.menu.listener()
                    main()
                elif PTF =='use modules/exploitdb':
                    core.menu.exploit_db()
                    main()
                elif PTF =='use modules/tools':
                    core.menu.tools()
                    main()
                elif PTF =='shell':
                    core.exploit.commands()
                    main()
                elif PTF == 'show modules':
                    core.help.modules()
                    main()
                elif PTF =='ipconfig':
                    core.exploit.ip1()
                    main()
                elif PTF =='show options':
                    core.help.help()
                    main()
                elif PTF =='update':
                    core.exploit.update()
                    main()
                elif PTF =='about':
                    core.banner.info()
                    main()
                elif PTF =='credits':
                    core.banner.credits()
                    main()
                elif PTF =='banner':
                    clean(),banner(),ptf(),main()
                elif PTF =='clear':
                    core.menu.exploit.clean()
                    main()
                elif PTF =='exit':
                    core.banner.exits()
                    exit()
                else:
                    print "Wrong Command => ", PTF
                    print ""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"
                    main()
            except(KeyboardInterrupt):
                print("\n"+R+"[*] (Ctrl + C ) Detected, Trying To Exit ...\n" )
                time.sleep(2)
                print(""+G+"[*] Thank You For Using Pentest Framework =)\n" )
                time.sleep(3)
                exit()
