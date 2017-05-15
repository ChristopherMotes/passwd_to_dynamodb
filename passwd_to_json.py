#!/usr/bin/python
import os
import json
import boto3

HOSTNAME = os.uname()[1]
PasswdObject = open("/Users/cmotes/python/passwd_to_json/passwd", 'r')
PasswdListofDicts = []
for line in PasswdObject:
	PasswdFields = line.strip().split(':')
	PerLineDict = { "Hostname" : {"S" : HOSTNAME } , "UserName" : { "S" : PasswdFields[0] } , "Password" : { "S" : PasswdFields[1] } , "UserId" : { "S" : PasswdFields[2] } , "GroupId"  : { "S" : PasswdFields[3] } , "Comment" : { "S" : PasswdFields[4] } , "HomeDirectory" : { "S" : PasswdFields[5] } , "Shell" : { "S" : PasswdFields[6] } }
	print json.dumps(PerLineDict)