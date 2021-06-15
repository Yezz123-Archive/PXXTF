#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)
 
from . import wpfile
from . import wpfpd
from . import wpconfig
from . import wplisting
from . import wplogin
from . import wprobots
from . import wpversion
from . import wpxmlrpc

from lib import wpprint

class wpgeneric:
	@staticmethod
	def run(agent,proxy,redir,time,url,cookie):
		wpxmlrpc.wpxmlrpc(agent=agent,proxy=proxy,
			redir=redir,time=time,url=url,cookie=cookie).run()
		wpconfig.wpconfig(agent=agent,proxy=proxy,
			redir=redir,time=time,url=url,cookie=cookie).run()
		wpfpd.wpfpd(agent=agent,proxy=proxy,
			redir=redir,time=time,url=url,cookie=cookie).run()	
		wpprint.wpprint().passs()
		wpfile.wpfile(agent=agent,proxy=proxy,
			redir=redir,time=time,url=url,cookie=cookie).run()
		wpprint.wpprint().passs()
		wplisting.wplisting(agent=agent,proxy=proxy,
			redir=redir,time=time,url=url,cookie=cookie).run()
		wplogin.wplogin(agent=agent,proxy=proxy,
			redir=redir,time=time,url=url,cookie=cookie).run()
		wpprint.wpprint().passs()
		wprobots.wprobots(agent=agent,proxy=proxy,
			redir=redir,time=time,url=url,cookie=cookie).run()
		wpprint.wpprint().passs()
		wpversion.wpversion(agent=agent,proxy=proxy,
			redir=redir,time=time,url=url,cookie=cookie).run()
		wpprint.wpprint().passs()