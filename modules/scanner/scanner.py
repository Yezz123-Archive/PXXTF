#!/usr/bin/env python
import sys, time, os , http.client , socket
import urllib2 as u2


class logging:
	f=""
	def __init__(self,_logfile):
		self._logfile=_logfile
		self.f = open(self._logfile, "w")
		self.f.write("Sensitive finder logs \n")
	def writelog(self,_message):
		try:
			self.f.write(_message) # Write a string to a file
		except IOError:
   	 		pass
   	def close(self):
   		self.f.close()


def proxycheck(_httpproxy,_proxy):
	try:
	  if _proxy:
	    print("[+] Testing Proxy...")
	    h2 = http.client.HTTPConnection(_httpproxy)
	    h2.connect()
	    print("[+] Proxy:",_httpproxy)
	    return 1
	except(socket.timeout):
	  print("[-] Proxy Timed Out")
	  sys.exit()
	  pass
	except(NameError):
	  print("[-] Proxy Not Given")
	  sys.exit()
	  pass
	except:
	  print("[-] Proxy Failed")
	  sys.exit()
	  pass

def timer():
  now = time.localtime(time.time())
  return "["+time.asctime(now)+"]"

def getWordlistLength(_wordlist):
        num_lines = sum(1 for line in open(_wordlist))
        return num_lines

def urlcheck(_url):
	try:
	       	print(("[!] Checking website " + _url + "..."))
	       	req = u2.Request(_url)
	       	u2.urlopen(req)
	       	print("[!] " +_url+" appears to be Online.\n")
   	except:
	        print("[-] Server offline or invalid URL")
	        sys.exit()

def printbanner():
	 print("""
""")

if __name__=='__main__':

	shellwordlist="shell.1337"
	backupwordlist="backups.1337"
	adminwordlist="admins.1337"
	dirwordlist="dir.1337"
	fileswordlist="files.1337"
	wordlist=""
	proxy = "None"
	proxy_supp=0
	count = 0
	mode = 0
	logging_support=1
	printbanner()

	if len(sys.argv) < 4 or len(sys.argv) > 7:
		print("Usage:"   + sys.argv[0] + " <http:url> -m <mode> -p <proxy> ")
		print("Example:" + sys.argv[0] + " http://host.com  -m shell -p 127.0.0.1:8118")
		exit()

	for arg in sys.argv:
		if arg == '-h':
			print("Usage:"   + sys.argv[0] + " <http:url> -m <mode> -p <proxy> ")
			print("Example:" + sys.argv[0] + " http://host.com  -m shell -p 127.0.0.1:8118")
			sys.exit(1)
		elif arg == '-p':
			proxy = sys.argv[count+1]
   			proxy_supp=1
   		elif arg == "-m":
   			mode = sys.argv[count+1]
  		count += 1

  	site = sys.argv[1]
	if site[:4] != "http":
  		site = "http://"+site
	if site.endswith("--"):
  		site = site.rstrip('--')
	if site.endswith("/*"):
  		site = site.rstrip('/*')
	urlcheck(site)

	if mode == "shell":
		wordlist=shellwordlist
	elif mode == "backup":
		wordlist=backupwordlist
	elif mode == "admin":
		wordlist=adminwordlist
	elif mode == "dir":
		wordlist=dirwordlist
	elif mode == "files":
		wordlist=fileswordlist
	else :
		print("[x] Mode not specified")
		exit()

	if not os.access(wordlist, os.F_OK):
		print((  "[x] File " + wordlist + " does not exist or "
			+ "you are not permitted to access to the file"))
		exit()

	proxycheck(proxy,proxy_supp)
	print(timer(),"[+] ["+mode+" Searching]")
	print("[+] Host:", site)
	print("[+] Wordlist " + wordlist + " has " + str(getWordlistLength(wordlist)) + " words\n\n")

	if proxy_supp != 0:
	    proxy_handler = u2.ProxyHandler({'http': 'http://'+proxy+'/'})
	    opener = u2.build_opener(proxy_handler)
	    u2.install_opener(opener)
  	else:
		pass

	if logging_support !=0:
		filename = site.replace ("http://","")
		filename2 = site.replace ("/","")
		logging_session=logging(filename2+".txt")
	else:
		pass

	with open(wordlist) as comfile:
		for line in comfile:
			line = line.strip("\r\n")
			req = u2.Request(sys.argv[1] + "/" + line)
			try:
				u2.urlopen(req)
			except u2.HTTPError as hr:
				if hr.code == 404:
					print(mode+": " + line.ljust(50,' ') + "[ 404 ]")
			except u2.URLError as ur:
				print("URL error:", ur.args)
				exit()
			except ValueError as vr:
				print("Value error:", vr.args)
				exit()
			except:
				print("Unknown exception: exit...")
				exit()
			else:
				print(mode+": " + line.ljust(50,' ') + "[ 200 OK ]")
				if logging_support !=0:
				   logging_session.writelog(mode+": " + line.ljust(50,' ') + "[OK]\n")
				else:
					pass
			try:
				pass
			except KeyboardInterrupt as kierr:
				print("\nInterrupted by user: (CTRL+C or Delete)")
				exit()
	logging_session.close()
