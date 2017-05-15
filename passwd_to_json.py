#!/usr/bin/python
import os
import json
PasswdObject = open("/Users/cmotes/python/passwd_to_json/passwd", 'r')
PasswdDict = {} 
for line in PasswdObject:
	PasswdFields = line.strip().split(':')
	PerLineDict = { "Name" : PasswdFields[0] , "Password" : PasswdFields[1] , "UserId" : PasswdFields[2] }
	print PerLineDict
