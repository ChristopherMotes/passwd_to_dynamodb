#!/usr/bin/python
import os
import json
PasswdObject = open("/Users/cmotes/python/passwd_to_json/passwd", 'r') 
for line in PasswdObject:
	print line.strip().split(':')