#!/usr/bin/python
import os
import json
HOSTNAME = os.uname()[1]
PasswdObject = open("/Users/cmotes/python/passwd_to_json/passwd", 'r')
PasswdListofDicts = []
for line in PasswdObject:
	PasswdFields = line.strip().split(':')
	PerLineDict = { "Hostname" : HOSTNAME , "UserName" : PasswdFields[0] , "Password" : PasswdFields[1] , "UserId" : PasswdFields[2] , "GroupId" : PasswdFields[3] , "Comment" : PasswdFields[4] , "HomeDirectory" : PasswdFields[5] , "Shell" : PasswdFields[6] }
	print json.dumps(PerLineDict)