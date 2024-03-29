#!/usr/bin/env python
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
import sys, os
class domain_map:
    def __init__(self):
        pass

    def atom(self, host, fname):
        import urllib.request, urllib.parse, urllib.error
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor('dnsdumpster.com'):
            try:
                content = urllib.request.urlretrieve(
                    'https://dnsdumpster.com/static/map/' + host + '.png',
                    fname)
                return True
            except BaseException:
                return "\tUnfortunately, the file could not be saved"

        else:
            return None

    def run(self):
        from random import randint
        import sys

        while True:
            host = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/domain_map"+G+"(set target)"+N+"): "))
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            rand = str(randint(0, 2000))
            fname = 'log/' + rand + '_domain_map.png'
            wread = self.atom(host, fname)

            if wread:
                print(('\tresult saved in ' + fname))
                print((""+G+""))
                os.system('firefox log/ ')
            elif wread is None:
                print("\t[-] Error Input")
                continue
            else:
                print(wread)
                break
            break
