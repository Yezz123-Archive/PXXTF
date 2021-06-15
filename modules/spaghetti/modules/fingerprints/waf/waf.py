#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

from . import aws
from . import baidu
from . import barracuda
from . import bigip
from . import binarysec
from . import cloudflare
from . import cloudfront
from . import dotdefender
from . import edgecast
from . import incapsula
from . import modsecurity
from . import profense
from . import radware
from . import paloalto
from . import sucuri
from . import urlscan
from . import varnish
from . import webknight

def Waf(headers):
	return (
		aws.Aws().Run(headers),
		baidu.Baidu().Run(headers),
		barracuda.Barracuda().Run(headers),
		bigip.Bigip().Run(headers),
		binarysec.Binarysec().Run(headers),
		cloudflare.Cloudflare().Run(headers),
		cloudfront.Cloudfront().Run(headers),
		dotdefender.Dotdefender().Run(headers),
		edgecast.Edgecast().Run(headers),
		paloalto.Paloalto().Run(headers),
		incapsula.Incapsula().Run(headers),
		modsecurity.Modsecurity().Run(headers),
		profense.Profense().Run(headers),
		radware.Radware().Run(headers),
		sucuri.Sucuri().Run(headers),
		urlscan.Urlscan().Run(headers),
		varnish.Varnish().Run(headers),
		webknight.Webknight().Run(headers)
		)