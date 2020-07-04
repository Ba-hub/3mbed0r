#!/usr/bin/env python


import sys
import pycolor
import os

pyc = pycolor.pyColor()

def banner():
	print '''  _____           _              _  ___
|___ / _ __ ___ | |__   ___  __| |/ _ \ _ __
  |_ \| '_ ` _ \| '_ \ / _ \/ _` | | | | '__|
 ___) | | | | | | |_) |  __/ (_| | |_| | |
|____/|_| |_| |_|_.__/ \___|\__,_|\___/|_|

                               %s				
'''%(pyc.cLine('YELLOW', "created by~ Ghosthub(b@b@y)"))

mainapk=None
def initstuff():
	argc = len(sys.argv)
	
	path=None
	if argc!=2:
		print pyc.Warn("Argument missing")
		print pyc.Info("Usage %s <apk-to-embed>")
		sys.exit()
	else:
		path=sys.argv[1]
		print(pyc.Info("Check file %s"%(path)))
		try:
			mainapk = path.split('/')[-1]
		except:
			pass
		
		if os.path.isfile(path):
			if os.access(path, os.R_OK):	
				print(pyc.Succ("File %s OK")%(path))
				if(mainapk.split('.')[-1]!='apk'):
					print(pyc.Warn("File(%s) doesn't appear to be application package, you want to continue?[y/n]"%mainapk))
					ch = raw_input("[y/n]> ")
					ch = ch.lower()
					if(ch=='y'):
						pass
					else:
						print(pyc.Warn("Exiting..."))
						sys.exit()						
			else:
				print(pyc.Err("Check the permissions"))
				sys.exit()
		else:
			print(pyc.Err("File(%s) doesnt exist"%(path)))
			sys.exit()
			
		z=os.system('cp %s %s'%(path, mainapk))
		if not (z):
			pass
		else:
			print pyc.Err("Couldn't make a copy of %s"%mainapk)
			sys.exit()
		
	return mainapk


def clean(mainapk):
	print pyc.Info("Cleaning workspace...")
	os.system('rm -rf temp.apk temp msf.rc %s %s'%(mainapk.split('.')[0],mainapk))



    