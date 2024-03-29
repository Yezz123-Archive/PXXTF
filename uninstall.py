#!/usr/bin/python

import sys
import os
import time


if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] Pentest Tools Framework installer must be run as root!!.\n\033[1;m""")

print(""" \033[1;36m
+---------------------------------------------------------------+
|                                                               |
|          [Pentest Tools Framework] [Uninstaller]              |
|                                                               |
+---------------------------------------------------------------=
  \033[1;m""")
print('\n\033[1;91m Remove modules PXXTF')
time.sleep(3)
os.system("rm -rf /opt/Pentest && rm -rf /usr/bin/ptf")
time.sleep(2)
print('\033[1;36m\nsucessfuly remove PTF\n')
