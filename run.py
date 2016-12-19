#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from credentials import *
from csvread import *
from sys import argv


script, filename = argv

#convert csv to refined
csvRead(filename)

filename=filename.split('.')
filename=filename[0].strip()

phone=''	
name=''
reg_no=''
	

myfile=open(filename+'Refined.txt','r')
myfile1=open(filename+'Status.txt','w+')
count=0
for line in myfile:
	line_copy=line
	if line=='\n':
		break	
	line=line.strip()
	raw=line.split(',')
	phone=raw[0]
	name=raw[1]
	reg_no=raw[2]
	
	if len(phone)<10 or len(phone)>10:
		response='INVALID'
		line_copy=line_copy.strip()
		line_copy=line_copy+','+response+'\n'
		myfile1.write(line_copy)
		count=count+1
		print count		
		continue

		

	text=name+' ji अपने गाडी'+reg_no+'की SERVICE शीघ्र  करवा ले।SHRI OM SAI AUTO 7349800023'

	url= 'http://bhashsms.com/api/sendmsg.php?user='+User+'&pass='+Password+'&sender='+Sender+'&phone='+phone+'&text='+text+'&priority=ndnd&stype=normal'

	response=requests.post(url)
	response=response.text
	response=response.strip()
	line_copy=line_copy.strip()
	line_copy=line_copy+','+response+'\n'
	myfile1.write(line_copy)
	count=count+1
	print count		
		
myfile.close()
myfile1.close()
