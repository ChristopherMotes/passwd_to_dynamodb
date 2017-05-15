#!/usr/bin/python
import os
import json
PasswdObject = open("/Users/cmotes/python/passwd_to_json/passwd", 'r')
PasswdListofDicts = []
for line in PasswdObject:
	PasswdFields = line.strip().split(':')
	PerLineDict = { "Name" : PasswdFields[0] , "Password" : PasswdFields[1] , "UserId" : PasswdFields[2] , "GroupId" : PasswdFields[3] , "Comment" : PasswdFields[4] , "HomeDirectory" : PasswdFields[5] , "Shell" : PasswdFields[6] }
	PasswdListofDicts.append(PerLineDict)
print json.dumps(PasswdListofDicts)