#!/usr/bin/python
import os
import json
import boto3
boto3.setup_default_session(profile_name='motes-acumera')
TIME_SINCE_EPOCH = calendar.timegm(time.gmtime())
TTL = TIME_SINCE_EPOCH * 10 * 60
dynamodb_clinet = boto3.client('dynamodb')
HOSTNAME = os.uname()[1]
PasswdObject = open("/Users/cmotes/python/passwd_to_json/passwd", 'r')
PasswdListofDicts = []
for line in PasswdObject:
	PasswdFields = line.strip().split(':')
	PerLineDict = { "Hostname" : {"S" : HOSTNAME } , "UserName" : { "S" : PasswdFields[0] } , "Password" : { "S" : PasswdFields[1] } , "UserId" : { "S" : PasswdFields[2] } , "GroupId"  : { "S" : PasswdFields[3] } , "HomeDirectory" : { "S" : PasswdFields[5] } , "Shell" : { "S" : PasswdFields[6] } , "TTL" : { "N" : TTL } }
	dynamodb_clinet.put_item(
		TableName = 'user_accounts',
		Item = PerLineDict
		) 
