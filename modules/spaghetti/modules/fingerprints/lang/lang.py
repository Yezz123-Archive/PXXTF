#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

from . import asp
from . import java
from . import php	
from . import python
from . import ruby

def Lang(content,headers):
	return (
		asp.Asp().Run(content,headers),
		java.Java().Run(content,headers),
		php.Php().Run(content,headers),
		python.Python().Run(content,headers),
		ruby.Ruby().Run(content,headers)
		)